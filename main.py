# TODO: Use sys argv or click to get airport name or id by cli
# TODO: Filter the specific aircraft and obtain its coordinates
# TODO: Set up a boundary of 60 km around that airport
# TODO: Filter using opensky and obtain statevectors within that boundary

import click
import sys
import os
import inspect
import numpy as np
import pandas as pd
from pathlib2 import Path
from opensky_api import OpenSkyApi

from errors.input_error import InputAirportError
from utils.misc import calculate_distance, calculate_buffer_geoposition
from utils.conversions import miles_to_km

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

    resultant_states = get_ac_within_bounds(airport=filtered_airport, radius=60)

    postprocess(resultant_states)


def inputDoesNotExist(id: int, name: str = None) -> None:
    frame = inspect.currentframe()
    message = "{}:{}: error: Input id '{}' does not exist.\n".format(
        __file__, frame.f_lineno, id
    )
    raise InputAirportError(message)


def get_airport(id: int, name: str = None) -> list:
    """
        Function that returns a list containing all data about the given id or name of the airport
        :param id: integer indicating the unique id of the airport as in our airports data.
        :param name: string indicating the name of the airport.
    """
    df = pd.read_csv(airport_data)

    if id in df["id"]:
        condition = df["id"] == id  # | (df["name"] == name)
        df = df[condition]

        return df.to_dict("records")[0]

    else:
        inputDoesNotExist(id)


def get_ac_within_bounds(airport: list, radius: int) -> list:
    """
        Function that returns a list of ac within the specified radius of the airport.
        :param airport: filtered airport data obtained from the csv file.
        :param radius: radius in nautical miles
    """
    # Convert from nautical miles to km
    radius_km = miles_to_km(radius)

    airport_lat = airport["latitude_deg"]
    airport_long = airport["longitude_deg"]

    # Obtain boundaries for api call
    lat_max, long_max = calculate_buffer_geoposition(
        airport_lat, airport_long, radius_km, 45
    )

    lat_min, long_min = calculate_buffer_geoposition(
        airport_lat, airport_long, radius_km, 45 + 180
    )

    api = OpenSkyApi()
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states(bbox=(lat_min, lat_max, long_min, long_max))

    return states


def postprocess(resultant_states):
    for s in resultant_states.states:
        print(
            "(Callsign: {}, Latitude: {}, Longitude: {}, Altitude: {}, Speed: {})".format(
                s.callsign, s.longitude, s.latitude, s.baro_altitude, s.velocity
            )
        )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter

    sys.exit(main())
