import click
from . import batch_geocoder as bg


@click.group()
def c4sfcensusgeocoder():
    """Command-line access to C4sf Census Geocoder.
    Run ``c4sfcensusgeocoder --help`` for a list of available commands.
    To get help with a specific command, run ``c4sfcensusgeocoder [COMMAND] --help``."""
    pass  # pragma: no cover


@c4sfcensusgeocoder.command(help="Testing Hello World.")
@click.option(
    "--test-text",
    required=True,
    help='The Text you want to print'
)
def hello_world(test_text):
    """Testing Hello World"""
    print(test_text)   


c4sfcensusgeocoder.add_command(hello_world)


if __name__ == '__main__':  # pragma: no cover
    c4sfcensusgeocoder()