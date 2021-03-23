# TODO: Use sys argv or click to get airport name or id by cli
# TODO: Filter the specific aircraft and obtain its coordinates
# TODO: Set up a boundary of 60 km around that airport
# TODO: Filter using opensky and obtain statevectors within that boundary

import click
import sys


@click.command()
@click.option("--id", type=int, default=1, help="Airport id.")
@click.option("--airport", type=str, help="The airport's name.")
def main(id, airport):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(id):
        click.echo("Hello %s!" % airport)


def get_airport():
    pass


def get_osky_data():
    pass


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter

    sys.exit(main())
