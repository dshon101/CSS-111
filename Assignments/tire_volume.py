"""
Write a Python program named tire_volume.py 
that reads from the keyboard the three numbers 
for a tire and computes and outputs the volume 
of space inside that tire
"""

# importing libraries
import math
from  datetime import datetime

# opened my volume.txt file at the top
with open('volume.txt', mode='a') as adding:
    # making a variable of next so that my code,
    # can loop if they are more than one user per time
    next_tire = ''
    # having the while loop to loop though so,
    # that we can append or text to our file
    while next_tire != 'done'.lower():
        next_tire = input('Would you like to check a Tire? (yes/done) ')
        # an if statememnt to continue runing the code, 
        # inside our while loop if the uses didn't enter done.
        if next_tire == 'yes'.lower():

            # having input from the use.
            width_of_tire = int(input('Enter the width of the tire in mm (eg: 205): '))
            aspectRatio_of_tire = int(input('Enter the aspect ratio of the tire in mm (eg: 60): '))
            diameter_of_tire = int(input('Enter the diameter of the wheel in inches (eg: 15): '))

            # calculating the volume of the tire
            # this is the calculation of pi * width of tire squared and aspect ratio,
            # i will call this first working
            first_working = (math.pi * (width_of_tire ** 2) * aspectRatio_of_tire)
            # this is the calculation of width of tire * aspect ratio + 2540*diameter,
            # i will call this second working
            second_working = (width_of_tire * aspectRatio_of_tire) + (2540 * diameter_of_tire)
            # now calculating the volume of the tire using the first and second working 
            volume = (first_working * second_working) / 1e10

            # printing the output with \n so that we can have one new,
            # line before and after we print the volume to the user
            print(f'\nThe approximate volume is {volume:.2f} liters.\n')

            # getting time whenevr it is used
            curent_date_and_time = datetime.now(tz=None)

            # the is an if statement to help append, evrey 
            # time the code loops through or is not terminited
            if next_tire != 'done'.lower():
                adding.write(str(curent_date_and_time))
                adding.write(', ')
                adding.write(str(width_of_tire))
                adding.write(', ')
                adding.write(str(aspectRatio_of_tire))
                adding.write(', ')
                adding.write(str(diameter_of_tire))
                adding.write(', ')
                adding.write(str(f'{volume:.2f}'))
                adding.write('\n')

            print('Next Tire Please!\n', '-' * 30)