""" Function to run the batch geocode using the censusgeocode wrapper """
import pandas as pd
import time
import censusgeocode as cg


def transform_input_df(df_input):
    """
    Try to clean this up (especially null row test with try/except pass)
    TODO: Alert User that there should only be 4 columns: street, city, state, and zip in the df_input
    """
    if df_input.isnull().values.any():
        print("The input dataframe has null value(s). Dropping the rows with at least one null value and proceeding...")
        df_input = df_input.dropna()
        print("Dropped the rows with any null value.")
    print("Dropping duplicates...")
    df_input = df_input.drop_duplicates()
    df_input['address'] = df_input[['street', 'city', 'state', 'zip']].apply(lambda x: ', '.join(x), axis=1)
    return df_input


def split_df_into_chunks(df_input, chunksize=500):
    list_of_df_input_chunks = []
    # Vincent's suggestion on making this partition better
    #     N = 10
    #     [df1 for _,df1 in df.groupby(np.arange(chunksize)//N)]
    for x in range(0, df_input.shape[0], chunksize):
        if x <= df_input.shape[0]:
            print("{index} is the current index".format(index=x))
            df_address_chunk = df_input.iloc[x: x + chunksize, :]
        else:
            print("{index} is the current index".format(index=x))
            df_address_chunk = df_input.iloc[x: df_input.shape[0], :]
        df_output_chunk_merged = geocode_wrapper(df_address_chunk)
        list_of_df_input_chunks.append(df_output_chunk_merged)
        print("sleeping...")
        time.sleep(0.5)
    return list_of_df_input_chunks


def geocode_wrapper(df_input_chunk):
    """
    Runs the censusgeocode wrapper and merges the results to the df_input_chunk table
    """
    print("calling censusgeocode addressbatch")
    print(df_input_chunk.iloc[0, :])
    dict_output_chunk = cg.addressbatch(df_input_chunk[["street", "city", "state", "zip"]].to_dict('records'))
    print("Finished calling censusgeocode addressbatch")
    df_output_chunk = pd.DataFrame.from_dict(dict_output_chunk)
    df_output_chunk_merged = df_input_chunk.merge(df_output_chunk, on='address')
    return df_output_chunk_merged


def run_geocoding(df_input, chunksize=500):
    transformed_input = transform_input_df(df_input)
    list_of_df_input_chunks = split_df_into_chunks(transformed_input, chunksize)
    combined_df = pd.concat(list_of_df_input_chunks, ignore_index=True)
    return combined_df
