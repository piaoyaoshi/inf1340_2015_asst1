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

    Inputs:

    Expected Outputs:

    Errors:

    """
    sides = raw_input ("Enter the number of sides on your polygon")

    if sides == "3" or sides.lower() == "three":
        print ("Your shape is a Triangle!")

    elif sides == "4" or sides.lower() == "four":
        print ("Your shape is a Quadrilateral!")

    elif sides == "5" or sides.lower() == "five":
        print ("Your shape is a Pentagon!")

    elif sides == "6" or sides.lower() == "six":
        print ("Your shape is a Hexagon!")

    elif sides == "7" or sides.lower() == "seven":
        print ("Your shape is a Heptagon!")

    elif sides == "8" or sides.lower() == "eight":
        print ("Your shape is an Octagon!")

    elif sides == "9" or sides.lower() == "nine":
        print ("Your shape is a Nonagon!")

    elif sides == "10" or sides.lower() == "ten":
        print ("Your shape is a Decagon!")

    else:
        print ("Please enter a whole number between 3 and 10")
        name_that_shape()




name_that_shape()