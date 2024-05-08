import math

def main():
        start_miles = float(input('What is your adometer value at the start of your Jouney? '))# Get an odometer value in U.S. miles from the user.
    
        end_miles = float(input('What is your adometer value at the end of your Jouney? '))# Get another odometer value in U.S. miles from the user.
    
        amount_gallons = float(input('What is you fuel amount in gallons? '))# Get a fuel amount in U.S. gallons from the user.
    
        mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)# Call the miles_per_gallon function and store
        # the result in a variable named mpg.
    
        lp100k = lp100k_from_mpg(mpg)# Call the lp100k_from_mpg function to convert the
        # miles per gallon to liters per 100 kilometers and
        # store the result in a variable named lp100k.
    
        print(f'{mpg:.1f} miles per gallon. \n{lp100k:.2f} liters per 100 kilometers.')# Display the results for the user to see.
        pass
    
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    miles_per_gallon = abs(end_miles - start_miles) / amount_gallons
    return miles_per_gallon
    
def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    mpg = 235.215 / mpg
    return mpg
    
# Call the main function so that
# this program will start executing.
main()