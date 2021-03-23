from opensky_api import OpenSkyApi


# read all a/c states in a boundary of switzerland

api = OpenSkyApi()
# bbox = (min latitude, max latitude, min longitude, max longitude)
states = api.get_states(bbox=(45.8389, 47.8229, 5.9962, 10.5226))
for s in states.states:
    print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))
