class Payment:
    def __init__(self, payment_id, order):
        self.payment_id = payment_id
        self.order = order
        self.amount = order.calculate_total()
        self.payment_method = None
        self.status = "Pending"

    def choose_payment_method(self):
        print("Choose payment method:")
        print("1. Cash")
        print("2. Credit Card")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.payment_method = "Cash"

        elif choice == "2":
            self.payment_method = "Credit Card"

        else:
            print("Invalid choice.")
            return False

        return True

    def process_payment(self):
        if self.payment_method is None:
            print("Please choose a payment method first.")
            return

        self.status = "Paid"
        print(f"Payment of {self.amount} EGP completed using {self.payment_method}.")

    def refund(self):
        if self.status == "Paid":
            self.status = "Refunded"
            print("Payment refunded.")
        else:
            print("Payment cannot be refunded.")

    def display_payment(self):
        print(f"Payment ID: {self.payment_id}")
        print(f"Amount: {self.amount} EGP")
        print(f"Payment Method: {self.payment_method}")
        print(f"Status: {self.status}")

    def pay_cash(self):
      amount_given = float(input("Enter amount paid: "))

      if amount_given < self.amount:
         print("Insufficient amount.")
         return False

      change = amount_given - self.amount
      self.status = "Paid"

      print(f"Payment successful.")
      print(f"Change: {change} EGP")

      return True

    def pay_by_card(self):
     card_number = input("Enter card number: ")

     if len(card_number) == 16 and card_number.isdigit():
          self.status = "Paid"
          print("Payment successful.")
          return True

     print("Invalid card number.")
     return False

