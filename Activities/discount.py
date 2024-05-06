"""
If the subtotal is $50 or greater and today is 
Tuesday or Wednesday, your program must subtract 
10% from the subtotal. Your program must then 
compute the total amount due by adding sales 
tax of 6% to the subtotal. Your program must 
print the discount amount if applicable, 
the sales tax amount, and the total amount due.
"""

from datetime import datetime

subtotal = float(input('What is your subtotal? '))
curent_date = datetime.now()

# day_of_the_weeek = curent_date.weekday()
day_of_the_weeek = 0

#print(curent_date, day_of_the_weeek, sep=' | ')

if day_of_the_weeek == 1 or 2:
    if subtotal >= 50:
        discount_amount = subtotal * 0.10
        subtotal_after_discount = subtotal - discount_amount
        sales_tax_amount = subtotal_after_discount * 0.06
        total_with_discount = subtotal_after_discount + sales_tax_amount
    print(f'Total: {total_with_discount:.2f}')
    # print(discount_amount)
elif day_of_the_weeek != (1 or 2):
    if subtotal < 50:
        sales_tax_amount = subtotal * 0.06
        total_without_discount = subtotal + sales_tax_amount
    print(f'Total: {total_without_discount:.2f}')    

