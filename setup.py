import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="c4sfcensusgeocoder",
    version="0.0.8",
    author="Data Science Working Group - Code for San Francisco",
    author_email="datascience@codeforsanfrancisco.org",
    description="Censusgeocoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sfbrigade/c4sf-censusgeocoder",
    install_requires=[
        "censusgeocode",
        "pandas",
        "click",
    ],
    py_modules=[
        "cli",
    ],
    entry_points='''
        [console_scripts]
        c4sfcensusgeocoder=c4sfcensusgeocoder.cli:main
    ''',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)