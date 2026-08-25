from Person import (Customer, Employee, Waiter, Chef, Cashier, Manager)
from menu import Menu
from order import Order
from Payment import Payment

customers = []
employees = []
payments = []

menu = Menu()

def add_customer():
    print("\n--- ADD CUSTOMER ---")

    name = input("Customer Name: ")
    phone = input("Customer Phone: ")

    customer_id = len(customers) + 1

    customer = Customer(customer_id,name,phone)

    customers.append(customer)

    print("Customer added!")


def add_employee():
    print("\n--- ADD EMPLOYEE ---")

    name = input("Employee Name: ")
    phone = input("Employee Phone: ")

    try:
        salary = float(input("Salary: "))
    except ValueError:
        print("Invalid salary.")
        return

    print("\n1. Waiter")
    print("2. Chef")
    print("3. Cashier")
    print("4. Manager")

    type_choice = input("Choose employee type: ").strip()

    employee_id = len(employees) + 1

    if type_choice == "1":
        employee = Waiter(employee_id, name, phone, salary)
    elif type_choice == "2":
        employee = Chef(employee_id, name, phone, salary)
    elif type_choice == "3":
        employee = Cashier(employee_id, name, phone, salary)
    elif type_choice == "4":
        employee = Manager(employee_id, name, phone, salary)
    else:
        print("Invalid employee type.")
        return

    employees.append(employee)

    print("Employee added!")


def view_all():
    print("\n--- CUSTOMERS ---")

    if customers:
        for customer in customers:
            customer.show_info()
    else:
        print("No customers found.")

    print("\n--- EMPLOYEES ---")

    if employees:
        for employee in employees:
            employee.show_info()
    else:
        print("No employees found.")


def make_customer_order():
    print("\n--- CREATE ORDER ---")

    try:
        customer_id = int(input("Enter Customer ID: "))
    except ValueError:
        print("Invalid Customer ID.")
        return

    # Find customer
    for customer in customers:
        if customer.customer_id == customer_id:
            order_id = input("Enter Order ID: ")
            order = Order(order_id)
            # Show available menu
            menu.display_menu()
            # Add items
            while True:
                item_name = input(
                    "\nEnter item name "
                    "(or type 'done' to finish): ").strip()
                if item_name.lower() == "done":
                    break
                try:
                    quantity = int(input("Enter quantity: "))
                except ValueError:
                    print("Invalid quantity.")
                    continue

                order.add_item(menu,item_name,quantity)

            # Make sure the order isn't empty
            if not order.items:
                print("Order is empty.")
                return

            # Add the actual Order object to the customer's orders
            customer.add_order(order)
            print("\nOrder created successfully!")
            order.display_order()
            return

    print("Customer not found!")


def make_payment():
    if not customers:
        print("No customers available.")
        return

    print("\n--- CUSTOMERS ---")

    for i in range(len(customers)):
        print(f"{i + 1}. {customers[i].name}")

    try:
        choice = int(input("Choose customer: "))
    except ValueError:
        print("Invalid choice.")
        return

    if choice < 1 or choice > len(customers):
        print("Invalid customer.")
        return

    customer = customers[choice - 1]

    if not customer.orders:
        print("This customer has no orders.")
        return

    print("\n--- CUSTOMER ORDERS ---")

    for i in range(len(customer.orders)):
     order = customer.orders[i]

     print(
        f"{i + 1}. "
        f"Order {order.order_id} "
        f"- {order.calculate_total():.2f} EGP "
        f"- {order.status}"
     )

    try:
        order_choice = int(input("Choose order: "))
    except ValueError:
        print("Invalid choice.")
        return

    if order_choice < 1 or order_choice > len(customer.orders):
        print("Invalid order.")
        return

    order = customer.orders[order_choice - 1]

    payment_id = input("Enter Payment ID: ")

    payment = Payment(payment_id,order)
    payments.append(payment)

    # Choose payment method
    while True:
        if payment.choose_payment_method():
            break

    # Process payment
    if payment.payment_method == "Cash":
        payment.pay_cash()

    elif payment.payment_method == "Credit Card":
        payment.pay_by_card()

    # Update order after successful payment
    if payment.status == "Paid":
        order.change_status("Paid")

        print("\nPayment successful!")

        payment.display_payment()
        payment.generate_receipt()

    else:
        print("\nPayment was not completed.")


def view_customer_orders():
    if not customers:
        print("No customers available.")
        return

    print("\n--- CUSTOMERS ---")

    for i in range(len(customers)):
      print(f"{i + 1}. {customers[i].name}")

    try:
        choice = int(input("Choose customer: "))
    except ValueError:
        print("Invalid choice.")
        return

    if choice < 1 or choice > len(customers):
        print("Invalid customer.")
        return

    customer = customers[choice - 1]

    customer.show_orders()


def run_employee_action():
    try:
        employee_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID.")
        return

    # Find employee
    for employee in employees:

        if employee.employee_id == employee_id:
            if isinstance(employee, Waiter):
                order_id = input("Enter Order ID: ")
                # Find the order
                for customer in customers:
                    for order in customer.orders:
                        if order.order_id == order_id:
                            employee.take_order(order)
                            return
                print("Order not found.")

            elif isinstance(employee, Chef):
                order_id = input("Enter Order ID: ")
                for customer in customers:
                    for order in customer.orders:
                        if order.order_id == order_id:
                            employee.cook_order(order)
                            return
                print("Order not found.")

            elif isinstance(employee, Cashier):
                print("Cashier payments should be "
                    "handled through the Payment system.")
                make_payment()

            elif isinstance(employee, Manager):
                employee.manage_staff()
                try:
                    bonus = float(input("Enter bonus: "))
                except ValueError:
                    print("Invalid bonus.")
                    return
                employee.give_bonus(bonus)
            return

    print("Employee not found!")


def main():

    while True:

        print("\n================================")
        print("   RESTAURANT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Customer")
        print("2. Add Employee")
        print("3. View All Data")
        print("4. Create Customer Order")
        print("5. View Customer Orders")
        print("6. Make Payment")
        print("7. Employee Perform Job")
        print("8. Display Menu")
        print("9. Manage Menu")
        print("10. Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            view_all()
        elif choice == "4":
            make_customer_order()
        elif choice == "5":
            view_customer_orders()
        elif choice == "6":
            make_payment()
        elif choice == "7":
            run_employee_action()
        elif choice == "8":
            menu.display_menu()
        elif choice == "9":
            menu.users_choices()
        elif choice == "10":
            print("Thank you for using our Restaurant Management System. Have a great day!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()