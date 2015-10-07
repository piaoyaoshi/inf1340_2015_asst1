#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:3,4,5

    Expected Outputs:Triangle,Quadrilateral,Pentagon

    Errors:None

    >>>3
    Triangle
    >>>12
    Error

    """

    # This is the dictionary containing key value pairs
    dict = {'3': 'Triangle', '4': 'Quadrilateral', '5': 'Pentagon', '6': 'Hexagon',
            '7': 'Heptagons', '8': 'Octagon', '9': 'Nonagon', '10': 'Decagon'}

    # This code asks for user input of number of sides
    number_of_sides = raw_input("Please enter the number of sides (only valid from 3 to 10):")

    # This code assess if the entered number is a key in the dictionary and if so prints the value
    if number_of_sides in dict.keys():
        print(dict[number_of_sides])
    else:
        print("Error")


name_that_shape()