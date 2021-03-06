#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# ERROR_MESSAGE in case of improper user input
ERROR_MESSAGE = 'I don\'t understand'

#  ========================================== Main Function =================================================


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Test Cases
    Inputs:Y,N
    Expected: Replace cables and try again.

    Inputs:Y,Y
    Expected: Clean terminals and try starting again.

    Inputs:N,Y
    Expected:Replace the battery.

    Inputs:N,N,Y
    Expected:Check spark plug connections.

    Inputs:N,N,N,N
    Expected: Engine is not getting enough fuel. Clean fuel pump.

    Inputs:N,N,N,Y,Y
    Expected: Get it in for service.

    Inputs:N,N,N,Y,N
    Expected: Check to ensure the choke is opening and closing.
    """

    check_silence()

# diagnose_car()

# ========================================== Helper Functions ================================================
# Each function represents a box on flowchart and supports re-usability

# This function is the first box in the flow chart


def check_silence():
    silent = raw_input("Is the car silent when you turn the key?")
    if silent == "Y":
        check_battery()
    elif silent == "N":
        check_noise()
    else:
        print (ERROR_MESSAGE)
        check_silence()

# This is the left side of the flowchart


def check_battery():
    corroded = raw_input("Are the battery terminals corroded?")
    if corroded == "Y":
        print ("Clean terminals and try starting again.")
    elif corroded == "N":
        print ("Replace cables and try again.")
    else:
        print (ERROR_MESSAGE)
        check_battery()

# Everything below is the right side of the flow chart


def check_noise():
    click = raw_input("Does the car make a clicking noise?")
    if click == "Y":
        print ("Replace the battery.")
    elif click == "N":
        check_crank()
    else:
        print (ERROR_MESSAGE)
        check_noise()


def check_crank():
    crank = raw_input("Does the car crank up but fail to start?")
    if crank == "Y":
        print ("Check spark plug connections.")
    elif crank == "N":
        check_engine()
    else:
        print (ERROR_MESSAGE)
        check_crank()


def check_engine():
    engine = raw_input("Does engine start and then die?")
    if engine == "Y":
        check_fuel()
    elif engine == "N":
        print ("Engine is not getting enough fuel. Clean fuel pump.")
    else:
        print (ERROR_MESSAGE)
        check_engine()


def check_fuel():
    fuel = raw_input("Does your car have fuel injection?")
    if fuel == "N":
        print ("Check to ensure the choke is opening and closing.")
    elif fuel == "Y":
        print ("Get it in for service.")
    else:
        print (ERROR_MESSAGE)
        check_fuel()



