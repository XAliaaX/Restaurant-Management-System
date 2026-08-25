class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "Pending"

    def add_item(self, item, price):
        self.items.append((item, price))

    def remove_item(self, item):
        for order_item in self.items:
            if order_item[0] == item:
                self.items.remove(order_item)
                break

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item[1]

        return total

    def change_status(self, status):
        self.status = status


# Create Order
order_id = input("Enter Order ID: ")
order = Order(order_id)

# Add Items
item = input("Enter item name: ")
price = float(input("Enter item price: "))
order.add_item(item, price)

item = input("Enter another item name: ")
price = float(input("Enter item price: "))
order.add_item(item, price)

print("\nOrder Items:", order.items)

# Calculate Total
print("Total:", order.calculate_total())

# Remove Item
item_to_remove = input("\nEnter item to remove: ")
order.remove_item(item_to_remove)

print("Order Items after removal:", order.items)
print("Total after removal:", order.calculate_total())

# Change Order Status
status = input("\nEnter new order status: ")
order.change_status(status)

print("Order Status:", order.status)