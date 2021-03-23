from math import sin, cos, sqrt, atan2, radians, degrees, asin


def calculate_distance(latitude1, longitude1, latitude2, longitude2) -> float:
    """
        Calculate distance between two lat,long points, return in km
    """

    # approximate radius of earth in km
    R = 6371.0

    lat1 = latitude1
    lon1 = longitude1
    lat2 = latitude2
    lon2 = longitude2

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def calculate_buffer_geoposition(latc, lonc, distance, bearing):
    """
        Function that takes in a center point and calculates a second geoposition based on distance [km] and bearing in [deg].
        The return is a second geolocation in deg, lat and long
    """

    R = 6378.1  # Radius of the Earth
    brng = radians(bearing)  # Bearing is 90 degrees converted to radians.
    d = distance  # Distance in km

    latc = radians(latc)
    lonc = radians(lonc)

    distanceToRadius = d / R

    new_lat = asin(
        sin(latc) * cos(distanceToRadius)
        + cos(latc) * sin(distanceToRadius) * cos(brng)
    )

    new_long = lonc + atan2(
        sin(brng) * sin(distanceToRadius) * cos(latc),
        cos(distanceToRadius) - sin(latc) * sin(new_lat),
    )

    return degrees(new_lat), degrees(new_long)
