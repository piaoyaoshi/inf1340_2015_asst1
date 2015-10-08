#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:y,n

    Expected Outputs:

    Errors:

    """
    # Each function represents a box in the flow chart
    # The functions will call the next function or "box" depending on user input
    # If input is not y or n the function will print "I don't understand" and re-call itself

    # This function is the first box in the flow chart
    def silent_fun():
        silent = raw_input("Is the car silent when you turn the key?")
        if silent == "y":
            corroded_fun()
        if silent == "n":
            click_fun()
        if silent != "y" or "n":
            print ("I don't understand")
            silent_fun()

    # This is the left side of the flowchart
    def corroded_fun():
        corroded = raw_input("Are the battery terminals corroded?")
        if corroded == "y":
            print ("Clean terminals and try starting again.")
            exit()
        if corroded == "n":
            print ("Replace cables and try again.")
            exit()
        if corroded != "y" or "n":
            print ("I don't understand")
            corroded_fun()

    # Everything below is the right side of the flow chart
    def click_fun():
        click = raw_input("Does the car make a clicking noise?")
        if click == "y":
            print ("Replace the battery.")
            exit()
        if click == "n":
            crank_fun()
        if click != "y" or "n":
            print ("I don't understand")
            click_fun()

    def crank_fun():
        crank = raw_input("Does the car crank up but fail to start?")
        if crank == "y":
            print ("Check spark plug connections.")
            exit()
        if crank == "n":
            engine_fun()
        if crank != "y" or "n":
            print ("I don't understand")
            crank_fun()

    def engine_fun():
        engine = raw_input("Does engine start and then die?")
        if engine == "y":
            fuel_fun()
        if engine == "n":
            print ("Engine is not getting enough fuel. Clean fuel pump.")
            exit()
        if engine != "y" or "n":
            print ("I don't understand")
            engine_fun()

    def fuel_fun():
        fuel = raw_input("Does your car have fuel injection?")
        if fuel == "n":
            print ("Check to ensure the choke is opening and closing.")
            exit()
        if fuel == "y":
            print ("Get it in for service")
            exit()
        if fuel != "y" or "n":
            print ("I don't understand")
            fuel_fun()

    silent_fun()

diagnose_car()


