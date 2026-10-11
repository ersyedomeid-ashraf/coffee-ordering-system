"""

Work flow of Project - Coffee Ordering System

1- Input from user (Select an option from Coffee Menu)

2- Process user choice (Add Coffee, View Order, Checkout, or Exit)

3- Result print (Display order details, total price, or confirmation message)


Cases : A - Add Coffee

Espresso - Add Espresso to order

Latte - Add Latte to order

Cappuccino - Add Cappuccino to order

Americano - Add Americano to order

Cases : B - View Order

Empty Order - No items in order

Items Available - Display all selected coffees with their prices

Total Price - Calculate and display the total amount


Cases : C - Checkout

Empty Cart - Your cart is empty

Yes - Order confirmed and cart cleared

No - Checkout cancelled and items remain in cart

Cases : D - Exit

Option 7 - Display goodbye message and terminate program

Cases : E - Invalid Choice

Invalid Option - Display error message and ask user to try again


"""


class Coffee:

    # initialize coffee with name and price

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    # initialize order with empty list

    def __init__(self):
        self.items = []

    # add coffee to order

    def add_item(self, coffee):

        self.items.append(coffee)

        print(f"Added {coffee.name} to your order.")

    # calculate total prize

    def total(self):

        return sum(item.price for item in self.items)
