class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"Phone updated to {self.phone} successfully!")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")


# Inherits from Person
class Customer(Person):
    def __init__(self, customer_id, name, phone):
        super().__init__(name, phone)

        self.customer_id = customer_id
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(
            f"Order {order.order_id} "
            f"added to {self.name}'s orders."
        )

    def show_info(self):
        print(f"\nCustomer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Number of Orders: {len(self.orders)}")

    def show_orders(self):
        if not self.orders:
            print("No orders found.")
            return

        print(f"\nOrders for {self.name}:")

        for order in self.orders:
            order.display_order()


# Inherits from Person
class Employee(Person):
    def __init__(self, employee_id, name, phone, salary, role):
        super().__init__(name, phone)

        self.employee_id = employee_id
        self.salary = salary
        self.role = role

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(
            f"Salary updated to "
            f"{self.salary:.2f} EGP successfully!"
        )

    def show_salary(self):
        print(f"Salary: {self.salary:.2f} EGP")

    def show_info(self):
        print(f"\nEmployee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary:.2f} EGP")


# Inherits from Employee
class Waiter(Employee):
    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary, "Waiter")

    def take_order(self, order):
        print(
            f"Waiter {self.name} "
            f"takes Order {order.order_id}."
        )


# Inherits from Employee
class Chef(Employee):
    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary, "Chef")

    def cook_order(self, order):
        print(
            f"Chef {self.name} "
            f"is cooking Order {order.order_id}."
        )


# Inherits from Employee
class Cashier(Employee):
    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary, "Cashier")

    def process_payment(self, payment):
        print(
            f"Cashier {self.name} "
            f"received {payment.amount:.2f} EGP."
        )


# Inherits from Employee
class Manager(Employee):
    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary, "Manager")

    def manage_staff(self):
        print(
            f"Manager {self.name} "
            f"is managing the staff."
        )

    def give_bonus(self, money):
        print(
            f"Bonus of {money:.2f} EGP "
            f"given by {self.name}."
        )