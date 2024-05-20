import random

def main():
    # create a lsit named numbers
   numbers = [16.2, 75.1, 52.3]
   
   # print numbers list
   print(f"Numbers: {numbers}")
   
   # calls the append_random_numbers function with only one argument to add one number to numbers
   append_random_numbers(numbers)
   
   # print numbers list
   print(f"Numbers: {numbers}")
 
   # calls the append_random_numbers function again with two arguments to add three numbers to numbers
   append_random_numbers(numbers, 3)
 
   # print numbers list
   print(f"Numbers: {numbers}")
 
 
def append_random_numbers(numbers_list, quantity=1):
  """
Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1
2.) Computes quantity pseudo random numbers by calling the random.uniform function.
3.) Rounds the quantity pseudo random numbers to one digit after the decimal.
4.) Appends the quantity pseudo random numbers onto the end of the numbers_list.
5.) At the bottom of your program, write an if statement that calls the main function. Then run your program and verify that your program works correctly.
 """
  for _ in range(quantity):
    random_number = random.uniform(0, 100)
    rounded = round(random_number, 1)
    numbers_list.append(rounded)
 
 
main()


"""
Add a function named append_random_words that meets the following criteria:Add statements in the main function that create a list of words, call the append_random_words function, and then print the list of words.Add something or change something in your program that you think would make your program better, easier for the user, more elegant, or more fun. Be creative.
Has two parameters: a list named words_list and an integer named quantity. The parameter quantity has a default value of 1Randomly selects quantity words from a list of words and appends the selected words at the end of words_list.
"""