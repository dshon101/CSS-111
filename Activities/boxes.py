"""
A manufacturing company needs a program 
that will help its employees pack manufactured 
items into boxes for shipping. Write a Python 
program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box
Your program must compute and print the number of 
boxes necessary to hold the items. This must be a 
whole number. Note that the last box may be packed with fewer items than the other boxes.

"""

import math

manufactured_items = int(input('How many items are manufactured? '))
items_per_box = int(input('How many items are you pack per box? '))

numberOf_boxes = manufactured_items / items_per_box

print(f'You need {math.ceil(numberOf_boxes)} boxes to pack.')