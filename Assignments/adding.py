with open('adding.txt', mode='a') as adding:
    user_product_bought = ''
    while user_product_bought != 'done':
        user_product_bought = input('What would you like to add: ')
        if user_product_bought != 'done':
            user_price_of_product = (input('What is the price? '))
            adding.write(user_product_bought)
            adding.write(', ')
            adding.write(user_price_of_product,)
            adding.write('\n')
        print('-' * 30)