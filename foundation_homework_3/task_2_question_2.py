chocolates = {
                'white': 1.50,
                 'milk': 1.20,
                 'dark': 1.80,
                'vegan': 2.00
}

chocolate = input('What item would you like to buy? ')

if chocolate == 'white':
    print(chocolates['white'])

elif chocolate == 'milk':
    print(chocolates['milk'])

elif chocolate == 'dark':
    print(chocolates['dark'])

elif chocolate == 'vegan':
    print(chocolates['vegan'])

else:
    print('Not available')
