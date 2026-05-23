# CSC500 - Module 6 Portfolio Milestone
# Online Shopping Cart
# Author: Andrew Friedrich


class ItemToPurchase:
    """Represents a single item that can be added to a shopping cart."""

    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ '
              f'${self.item_price} = ${self.item_quantity * self.item_price}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    """Represents a customer's shopping cart and the items it holds."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Append an ItemToPurchase to cart_items."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Remove the item whose name matches item_name."""
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                return
        print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        """Modify description, price, and/or quantity of a matching item.

        Only fields that differ from their default values on the incoming
        item are applied to the existing cart item.
        """
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                return
        print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        """Return the total quantity of all items in the cart."""
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self):
        """Return the total cost of all items in the cart."""
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        """Print the cart total in the required format, or empty notice."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
            return
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        print()
        for item in self.cart_items:
            item.print_item_cost()
        print()
        print(f'Total: ${self.get_cost_of_cart()}')

    def print_descriptions(self):
        """Print each item's description in the required format."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print('Item Descriptions')
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    """Display the menu and process user choices until 'q' is entered."""
    menu = (
        '\nMENU\n'
        'a - Add item to cart\n'
        'r - Remove item from cart\n'
        'c - Change item quantity\n'
        "i - Output items' descriptions\n"
        'o - Output shopping cart\n'
        'q - Quit\n'
    )

    valid_options = ('a', 'r', 'c', 'i', 'o', 'q')
    command = ''

    while command != 'q':
        print(menu)
        command = input('Choose an option:\n').strip().lower()

        # Re-prompt on invalid input
        while command not in valid_options:
            command = input('Choose an option:\n').strip().lower()

        if command == 'o':
            print('\nOUTPUT SHOPPING CART')
            cart.print_total()
        elif command == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        # a, r, c are accepted as valid menu choices but will be
        # implemented in a later module per the assignment instructions.


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print(f'Customer name: {customer_name}')
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == '__main__':
    main()
