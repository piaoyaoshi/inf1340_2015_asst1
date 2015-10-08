#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

""" Lakshmi bought some shares sometime ago. She later sold them.
    On both occasions, she had to pay the stockbroker for his/her services.

    Now, she is having troubles calculating how much she made or lost during the transaction.
    This program fixes that! Now, she's soooo happy :)
"""


commission_rate = 0.03
stock_quantity = 2000
cost_price = 900
selling_price = 942.75

stock_cost = stock_quantity * cost_price  #amount stock was bought
purchase_commission = commission_rate * stock_cost  #amount paid to stock broker for buying
amount_spent = stock_cost + purchase_commission

stock_income = stock_quantity * selling_price #amount the stock was sold
selling_commission = commission_rate * stock_income #amount paid to stock broker for selling
amount_received = stock_income - selling_commission

profit = amount_received - amount_spent


print('Lakshmi spent %.2f getting the stock' % amount_spent)
print('She received %.2f after selling the stock' % amount_received)
print('Now she has a profit of %.2f' % profit),
print('(negative sign means a loss).')