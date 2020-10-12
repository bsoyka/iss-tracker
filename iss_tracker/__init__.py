import datetime
import json
import math
import threading
import tkinter
import urllib.request

import requests
from PIL import Image, ImageTk

prev_lat, prev_long, prev_time, prev_speed = 0, 0, 0, 0


def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians

    # theta = longitude
    theta1 = long1 * degrees_to_radians
    theta2 = long2 * degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) =
    # sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(
        phi1
    ) * math.cos(phi2)
    arc = math.acos(cos)

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    return arc


def start():
    top = tkinter.Tk()
    top.title("ISS Tracker")

    def counter_label(label):
        def count():
            global prev_lat
            global prev_long
            global prev_time
            global prev_speed
            req = requests.get("http://api.open-notify.org/iss-now.json")

            obj = req.json()
            lat = float(obj["iss_position"]["latitude"])
            long = float(obj["iss_position"]["longitude"])
            timestamp = int(obj["timestamp"])
            time_change = timestamp - prev_time
            distance_moved = (
                distance_on_unit_sphere(prev_lat, prev_long, lat, long) * 4164
            )
            speed = distance_moved * 3600

            if time_change != 1 or distance_moved > 5:
                label.config(
                    text="Estimated speed: {} mph\nLatitude: {}\nLongitude: {}".format(
                        prev_speed, lat, long
                    )
                )
            else:
                label.config(
                    text="Estimated speed: {} mph\nLatitude: {}\nLongitude: {}".format(
                        speed, lat, long
                    )
                )
                prev_speed = speed
            prev_lat, prev_long, prev_time = lat, long, timestamp
            label.after(1000, count)

        count()

    title = tkinter.Label(
        top, height=1, width=50, font=("Arial", 25, "bold"), text="ISS Tracker"
    )
    title.pack()
    label = tkinter.Label(top, height=3, width=50, font=("Arial", 20))
    label.pack()
    counter_label(label)
    top.mainloop()
