#!/usr/bin/python36

import os, sys, getopt

try:
    import numpy
except ImportWarning:
    "It is recommended to have 'numpy' installed for 'python3.6'."
    pass

class Residential_House:
    """\
    This is a class object that represents a real world 'residential home'.
    """
    #TBA: Please only add to these if you also have a functional purpose in mind for it.
    #TBA: The act of assigning a value to a container/variable is the act of using/assigning
    #TBA: private memory. Literally. Let's not waste it.
    def __init__(self, address, stories, height, width, property_area,
                 windows, doors, power_outlets, bathrooms, bedrooms,
                 total_rooms, property_value):
        self.address = address
        self.stories = stories
        self.height = height
        self.width = width
        self.property_area = property_area
        self.property_value = property_value
        self.power_outlets = power_outlets
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.total_rooms = total_rooms
        self.windows = windows
        self.doors = doors

