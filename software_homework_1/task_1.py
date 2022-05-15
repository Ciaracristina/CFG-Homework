"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):
        self.total_items = list()  # {'item': 'price'}
        self.discount_percentage = 0

    def add_item(self, item, price):
        self.total_items.append({item: price})

    def remove_item(self, item):
        for item_and_price in self.total_items:
            current_item = next(iter(item_and_price.keys()))
            if current_item == item:
                self.total_items.remove(item_and_price)
                break

    def apply_discount(self, discount_percentage):
        self.discount_percentage = discount_percentage
        print('Discount of {}% applied'.format(discount_percentage))

    def get_total(self):
        running_total = 0
        for item_and_price in self.total_items:
            current_item_price = next(iter(item_and_price.values()))
            running_total += current_item_price
        return running_total * (100-self.discount_percentage)/100

    def show_items(self):
        for item_and_price in self.total_items:
            current_item = next(iter(item_and_price.keys()))
            current_item_price = next(iter(item_and_price.values()))
            print('{} ... £{:.2f}'.format(current_item, current_item_price))
        print('DISCOUNT ... {}%'.format(self.discount_percentage))
        print('TOTAL ... £{:.2f}'.format(self.get_total()))

    def reset_register(self):
        self.total_items.clear()
        self.discount_percentage = 0
        print('Register reset')


# EXAMPLE code run:
print('Initialising cash register')
cash_register = CashRegister()
print()

# ADD
print('Adding items')
cash_register.add_item('cheese', 3.00)
cash_register.add_item('cheese', 3.00)
cash_register.add_item('sourdough', 4.00)
cash_register.add_item('milk', 2.00)
cash_register.add_item('chocolate', 2.50)
print(cash_register.total_items)
print()

# REMOVE
print('Removing items')
cash_register.remove_item('cheese')
cash_register.remove_item('sourdough')
print(cash_register.total_items)
print()

# APPLY DISCOUNT
print('Applying discount')
cash_register.apply_discount(10)
print()

# TOTAL
print('Calculating total')
print(cash_register.get_total())
print()

# RECEIPT
print('Showing items')
cash_register.show_items()
print()

# RESET
print('Resetting register')
cash_register.reset_register()
cash_register.show_items()
print()
