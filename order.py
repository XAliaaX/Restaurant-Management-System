class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "Pending"

    def add_item(self, menu, item_name, quantity):
        # Check that the quantity is valid
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return False

        # Search for the item in the menu
        for menu_item in menu.menu:

            if menu_item.name.lower() == item_name.lower():

                # Check whether the item is available
                if not menu_item.availability:
                    print(f"{menu_item.name} is currently unavailable.")
                    return False

                # Check if the item is already in the order
                for order_item in self.items:
                    if order_item[0].lower() == menu_item.name.lower():

                        # Increase its quantity
                        order_item[2] += quantity

                        print(
                            f"{quantity} more {menu_item.name}(s) "
                            "added to the order."
                        )
                        return True

                # Add a new item
                self.items.append(
                    [menu_item.name, menu_item.price, quantity]
                )

                print(f"{quantity} {menu_item.name}(s) added to the order.")
                return True

        # Item does not exist in the menu
        print("Item not found in the menu.")
        return False

    def remove_item(self, item_name):
        # Search for the item in the order
        for order_item in self.items:

            if order_item[0].lower() == item_name.lower():
                self.items.remove(order_item)

                print(f"{order_item[0]} removed from the order.")
                return True

        print("Item not found in the order.")
        return False

    def calculate_total(self):
        total = 0

        # Price × quantity for every item
        for item in self.items:
            total += item[1] * item[2]

        return total

    def change_status(self, status):
        self.status = status

    def display_order(self):
        print("\n---------- ORDER ----------")
        print(f"Order ID: {self.order_id}")

        if not self.items:
            print("No items in the order.")

        else:
            for item in self.items:
                name = item[0]
                price = item[1]
                quantity = item[2]
                subtotal = price * quantity

                print(
                    f"{name} | "
                    f"Price: {price:.2f} EGP | "
                    f"Quantity: {quantity} | "
                    f"Subtotal: {subtotal:.2f} EGP"
                )

        print(f"Total: {self.calculate_total():.2f} EGP")
        print(f"Status: {self.status}")
        print("---------------------------")