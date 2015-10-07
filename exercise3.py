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

    Inputs:

    Expected Outputs:

    Errors:

    """
    error_msg = 'I do not understand, please enter Y / N only'

    check_silence = raw_input('Is the car silent when you turn the key? (Y/N)')

    while not ((check_silence == 'Y') or (check_silence == 'N')):
        print(error_msg)
        check_silence = raw_input('Is the car silent when you turn the key? (Y/N)')
    if check_silence == 'Y':

        check_battery = raw_input('Are the battery terminals corroded? (Y/N)')

        while not ((check_battery == 'Y') or (check_battery == 'N')):
            print(error_msg)
            check_battery = raw_input('Are the battery terminals corroded? (Y/N)')
        if check_battery == 'Y':
            print('Clean terminals and try starting again')
        if check_battery == 'N':
            print('The battery cables may be damaged.Replace cables and try again')

    if check_silence == 'N':

        check_noise = raw_input('Does the car make a clicking noise? (Y/N)')

        while not ((check_noise == 'Y') or (check_noise == 'N')):
            print(error_msg)
            check_noise = raw_input('Does the car make a clicking noise? (Y/N)')
        if check_noise == 'Y':
            print('Replace the battery')
        if check_noise == 'N':

            check_crank = raw_input('Does the car crank up but fail to start? (Y/N)')

            while not ((check_crank == 'Y') or (check_crank == 'N')):
                print(error_msg)
                check_crank = raw_input('Does the car crank up but fail to start? (Y/N)')
            if check_crank == 'Y':
                print('Check spark plug connections.')
            if check_crank == 'N':

                check_engine = raw_input('Does the engine start and then die? (Y/N)')

                while not ((check_engine == 'Y') or (check_engine == 'N')):
                    print(error_msg)
                    check_engine = raw_input('Does the engine start and then die? (Y/N)')
                if check_engine == 'N':
                    print('Engine is not getting enough fuel. Clean fuel pump')
                if check_engine == 'Y':

                    check_fuel = raw_input('Does your car have fuel injection? (Y/N)')

                    while not ((check_fuel == 'Y') or (check_fuel == 'N')):
                        print(error_msg)
                        check_fuel = raw_input('Does your car have fuel injection? (Y/N)')
                    if check_fuel == 'Y':
                        print('Get it in for service')
                    if check_fuel == 'N':
                        print('Check to ensure the choke is opening and closing.')



diagnose_car()