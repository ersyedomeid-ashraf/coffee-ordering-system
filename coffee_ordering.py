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

    # show oder summary

    def show_order(self):

        if not self.items:

            print("No items in order.")
            return

        print("\n your order: ")

        for i, item in enumerate(self.items, 1):

            print(f"{i}. {item.name} - ${item.price}")

        print(f"Total: ${self.total()}\n")

    # handle checkout process

    def checkout(self):

        if not self.items:
            print("Your cart is empty.")

            return

        self.show_order()

        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm == "yes":
            print("Order confirmed! Thank you. ")

            self.items.clear()

        else:
            print("Checkout cancelled.")


# display menu and handle user input.


def main():

    menu = [
        Coffee("Espresso", 22.5),
        Coffee("Latte", 36.5),
        Coffee("Cuppuccino", 45.0),
        Coffee("Americano", 35.0),
    ]

    order = Order()

    # User interaction

    while True:
        print("\n--- Coffee Menu ---")

        for i, item in enumerate(menu, 1):

            print(f"{i}. {item.name} - $ {item.price}")

        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4"]:
            order.add_item(menu[int(choice) - 1])

        elif choice == "5":
            order.show_order()

        elif choice == "6":
            order.checkout()

        elif choice == "7":
            print("Thanks for visiting. Goodbye!")

            break

        else:

            print("Invalid choice. Try again")


if __name__ == "__main__":

    main()
