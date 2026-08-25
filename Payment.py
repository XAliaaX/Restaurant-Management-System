class Payment:
    def __init__(self, payment_id, order):
        # Store the payment ID and the order associated with this payment
        self.payment_id = payment_id
        self.order = order

        # Get the total amount from the order
        self.amount = order.calculate_total()

        # Payment method will be selected later
        self.payment_method = None

        # New payments start with a Pending status
        self.status = "Pending"

    def choose_payment_method(self):
        # Display the available payment methods
        print("Choose payment method:")
        print("1. Cash")
        print("2. Credit Card")

        choice = input("Enter your choice: ")

        # Set the payment method based on the user's choice
        if choice == "1":
            self.payment_method = "Cash"

        elif choice == "2":
            self.payment_method = "Credit Card"

        else:
            # Return False if the user enters an invalid choice
            print("Invalid choice.")
            return False

        return True

    def process_payment(self):
        # The user must choose a payment method before paying
        if self.payment_method is None:
            print("Please choose a payment method first.")
            return

        # Mark the payment as completed
        self.status = "Paid"
        print(f"Payment of {self.amount} EGP completed using {self.payment_method}.")

    def refund(self):
        # A payment can only be refunded if it was already paid
        if self.status == "Paid":
            self.status = "Refunded"
            print("Payment refunded.")
        else:
            print("Payment cannot be refunded.")

    def display_payment(self):
        # Display all important information about the payment
        print(f"Payment ID: {self.payment_id}")
        print(f"Amount: {self.amount} EGP")
        print(f"Payment Method: {self.payment_method}")
        print(f"Status: {self.status}")

    def pay_cash(self):
        # Ask the customer how much cash they are giving
        amount_given = float(input("Enter amount paid: "))

        # Check whether the customer gave enough money
        if amount_given < self.amount:
            print("Insufficient amount.")
            return False

        # Calculate the money that should be returned to the customer
        change = amount_given - self.amount

        # Mark the payment as paid
        self.status = "Paid"

        print("Payment successful.")
        print(f"Change: {change} EGP")

        return True

    def pay_by_card(self):
        # Ask the customer to enter their card number
        card_number = input("Enter card number: ")

        # Check that the card number contains exactly 16 digits
        if len(card_number) == 16 and card_number.isdigit():
            self.status = "Paid"
            print("Payment successful.")
            return True

        # Reject the payment if the card number is invalid
        print("Invalid card number.")
        return False

    def generate_receipt(self):
      print("\n================================")
      print("            RECEIPT")
      print("================================")

      print(f"Order ID: {self.order.order_id}")
      print(f"Payment ID: {self.payment_id}")

      print("\nItems:")
    
      for item in self.order.items:
         name = item[0]
         price = item[1]
         quantity = item[2]

         subtotal = price * quantity

         print(
            f"{name} x {quantity} "
            f"- {subtotal:.2f} EGP"
         )

      print("--------------------------------")
      print(f"Total: {self.amount:.2f} EGP")
      print(f"Payment Method: {self.payment_method}")
      print(f"Payment Status: {self.status}")
      print("================================")
