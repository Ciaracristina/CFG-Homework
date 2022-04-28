my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5

if my_money > boat_cost:
    print('You can afford the boat hire')

else:
    print('You cannot afford the board hire')

# The input needed set to float as it is going to be dealing with numbers and the less than symbol was wrong in the if statement.
