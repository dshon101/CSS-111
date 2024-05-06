"""
This code computes the volume and suface area for cans.
"""


import math


# built_in_functions = 'input, float, lower, print'
# x = 2.2
# y = 4.2
# sum = x * y
# rounded_sum = round(sum, 2)
# squreroot_rounded_sum = round(math.sqrt(rounded_sum), 2)
# print(squreroot_rounded_sum)

# name = 'Demetrious Shoniwa'
# length = len(name)

# name2 = name.upper()

# print(f'{name2} has {length} letters.')
# print(name, 'has', length, 'letters')
# print(name2 + ' has ' + str(length) + ' letters')

# manufactured_item = int(input('Enter number of Manufactured Items? '))
# items_per_box = int(input('Enter the number of items in boxes?'))

# boxes = math.ceil(manufactured_item / items_per_box)
# print(f'For {manufactured_item} they need {boxes} boxes.')

""" we could use list variables for the can_name, can_radius, can_height and  can_cost
can_name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 7.62, 8.10]
can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
"""
def main():
    print(f'For #1 Picnic The volume is {compute_volume(6.83, 10.16):.2f} and the suface aree is {compute_surface_area(6.83, 10.16):.2f}')
    print(f'For #1 Tall The volume is {compute_volume(7.78, 11.91):.2f} and the suface aree is {compute_surface_area(7.78, 11.91):.2f}')

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = (2 * math.pi) * radius * (radius + height)
    return surface_area

main()










