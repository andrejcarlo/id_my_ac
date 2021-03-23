# TODO: Use sys argv or click to get airport name or id by cli
# TODO: Filter the specific aircraft and obtain its coordinates
# TODO: Set up a boundary of 60 km around that airport
# TODO: Filter using opensky and obtain statevectors within that boundary

import click
import sys
import pandas as pd
from pathlib2 import Path
import os
import inspect
from errors.input_error import InputAirportError

data_dir = Path.cwd().joinpath("data")
filename = "airports.csv"
airport_data = data_dir.joinpath(filename)


@click.command()
@click.option("--id", required=True, type=int, help="Airport id.")
@click.option("--name", type=str, help="The airport's name.")
def main(id, name):
    # do some checks for id and airport options, what happens when they're not expected type
    # return airport not found

    filtered_airport = get_airport(id, name)


def inputDoesNotExist(id: int, name: str = None) -> None:
    frame = inspect.currentframe()
    message = "{}:{}: error: Input id '{}' does not exist.\n".format(
        __file__, frame.f_lineno, id
    )
    raise InputAirportError(message)


def get_airport(id: int, name: str = None) -> list:
    """
        Function that returns a list containing all data about the given id or name of the airport
        :param id: integer indicating the id of the airport as in our airports data.
    """
    df = pd.read_csv(airport_data)

    if id in df["id"]:
        condition = df["id"] == id  # | (df["name"] == name)
        df = df[condition]

        return df.to_dict("records")

    else:
        inputDoesNotExist(id)


def get_osky_data():
    pass


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter

    sys.exit(main())
