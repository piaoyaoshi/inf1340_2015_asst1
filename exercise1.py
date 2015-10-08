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

money = 0
commission_rate = 0.03 #same commission during purchase and sale

qty_bought = 2000
purchase_price = 900

qty_sold = 2000
sell_price = 942.73

book_value = qty_bought * purchase_price #shares cost value
purchase_fee = book_value * commission_rate #commision paid to stockbroker for purchase

amount_received = qty_sold * sell_price #shares selling value
sell_fee = amount_received * commission_rate #commision paid to stockbroker for sale

money = money + amount_received - sell_fee - purchase_fee
profit = (amount_received - book_value) - sell_fee - purchase_fee

print('Lakshmi had $'),
print(money),
print('left, and she made a profit of $'),
print('%.2f' % profit),
print('(negative sign means a loss).')
