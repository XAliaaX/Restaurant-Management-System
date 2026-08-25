class MenuItem:
    def __init__(self, name, price, category, availability=True):
        self.name = name
        self.price = price
        self.category = category
        self.availability = availability


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("Pizza", 245.67, "food"),
            MenuItem("Burger", 179.98, "food"),
            MenuItem("Coffee", 115.34, "drink"),
            MenuItem("Tea", 40.56, "drink", False),
            MenuItem("Seafood", 378.23, "food"),
            MenuItem("Pasta", 169.99, "food"),
            MenuItem("Soda", 25.50, "drink"),
            MenuItem("Salad", 120.87, "food"),
            MenuItem("Juice", 55.75, "drink"),
            MenuItem("Ice Cream", 80.00, "food"),
        ]

    def add_to_menu(self):
        name = input("Enter item name: ").strip()

        while True:
            try:
                price = float(input("Enter price: "))
                break
            except ValueError:
                print("Invalid price!, Enter a valid number: ")

        while True:
            category = input("Enter category (food/drink): ").strip().lower()
            if category in ["food", "drink"]:
                break
            print("Invaild input!, Enter (food/drink): ")

        item = MenuItem(name, price, category)
        self.menu.append(item)
        print("Item added!")

    def remove_from_menu(self):
        name = input("Item to be removed: ").lower()

        for item in self.menu:
            if item.name.lower() == name:
                self.menu.remove(item)
                print(f"{item.name} is removed!")
                return

        print("Item not found")

    def search_for_item(self):
        name = input("Item to be searched: ").lower().strip()

        for item in self.menu:
            if item.name.lower() == name:
                print(f"""
             Name: {item.name}
             price: {item.price:.2f} EGP
             Category: {item.category}
             Available: {item.availability}""")
                return
        print("Item NOT found!")

    def display_menu(self):
        print("\n---------- MENU ----------")

        for item in self.menu:
            print(
                f"Name: {item.name} - "
                f"Price: {item.price:.2f} EGP - "
                f"Category: {item.category} - "
                f"Available: {item.availability}"
            )

        print("-----------------------")

    def change_availability(self):
        name = input("Enter item: ").strip().lower()

        for item in self.menu:
            if item.name.lower() == name:
                while True:
                    status = input("Choose Availability (True/False):  ").capitalize()
                    if status in ["True", "False"]:
                        item.availability = status == "True"
                        print(f"Updated to {item.availability}")
                        return
                    else:
                        print("Invaild input!, Enter(True/False): ")
        print("Item NOT found!")

    def users_choices(self):
        actions = {
            "1": self.add_to_menu,
            "2": self.remove_from_menu,
            "3": self.search_for_item,
            "4": self.display_menu,
            "5": self.change_availability,
        }
        while True:
            choice = input("""
              --- What do you want to do? ---

                1. Add to menu
                2. Remove from the menu
                3. Search in the menu
                4. Display the menu
                5. Change Availability
                6. Exit

              Enter your choice: """).strip()

            if choice == "6":
                print("Exiting Menu Management. Thank you!")
                break

            action = actions.get(choice)

            if action:
                action()
            else:
                print("Invalid choice!")



