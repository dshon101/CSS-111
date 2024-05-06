"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.

"""

name = str(input('What is your name? '))
age = int(input('What is your age?'))

high_rate = (220 - age) # calculating the maximum heart rate using the user's age.
slowest_rate = high_rate * 0.65
fastest_rate = high_rate * 0.85

print(f'{name} When you exercise to strengthen your heart, you should keep your heart rate between {slowest_rate:.0f} and {fastest_rate:.0f} beats per minute.')