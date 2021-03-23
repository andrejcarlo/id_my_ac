from opensky_api import OpenSkyApi
import numpy as np


def read_all_ac_bd():
    # read all a/c states in a boundary of switzerland

    api = OpenSkyApi()
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states(bbox=(45.8389, 47.8229, 5.9962, 10.5226))
    for s in states.states:
        print(
            "(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity)
        )


def read_all_ac():

    api = OpenSkyApi()
    states = api.get_states()
    for s in states.states:
        # print(
        #     "(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity)
        # )
        print(s)


if __name__ == "__main__":
    read_all_ac()
