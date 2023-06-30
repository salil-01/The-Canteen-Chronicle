# list of all the snack
itemsList = [
    {"id": 1, "name": "Samosa", "price": 250, "availability": "Yes"},
    {"id": 2, "name": "Chips", "price": 50, "availability": "Yes"},
    {"id": 3, "name": "Lassi", "price": 100, "availability": "Yes"}
]


# list of sold snacks
soldSnacks = []


# generate unique id for each snack
def generate_unique_id():
    max_id = max(item["id"] for item in itemsList) if itemsList else 0
    return max_id + 1


# display user input options in cli
def display_menu():
    print("***** Mumbai Munchies: The Canteen Chronicle *****")
    print("1. View Inventory")
    print("2. Add Snack")
    print("3. Update Snack Availability")
    print("4. Sell/Remove Snack")
    print("5. View Sold Snacks")
    print("6. Exit")


# see all the snacks in inventory
def view_inventory():
    print("***** Snack Inventory *****")
    for item in itemsList:
        print(
            f"ID: {item['id']}\tName: {item['name']}\tPrice: {item['price']}\tAvailability: {item['availability']}")
    print()


# add a snack in inventory
def add_snack():
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = "Yes"
    item_id = generate_unique_id()
    item = {"id": item_id, "name": name,
            "price": price, "availability": availability}
    itemsList.append(item)
    print("Snack added successfully!\n")


# update existing snack in inventory
def update_snack():
    item_id = int(input("Enter the ID of the snack to update: "))
    for item in itemsList:
        if item["id"] == item_id:
            new_availability = input("Enter updated availability (Yes/No): ")
            item["availability"] = new_availability.capitalize()
            print("Snack availability updated successfully!\n")
            return
    print("Snack not found!\n")


# remove/selling existing snack from inventory
def sell_snack():
    item_id = int(input("Enter the ID of the snack to remove: "))
    for index, item in enumerate(itemsList):
        if item["id"] == item_id:
            if item["availability"] == "No":
                print("This snack is not available and cannot be sold.\n")
                return
            soldSnacks.append(item)
            del itemsList[index]
            print("Snack Sold successfully!\n")
            return
    print("Snack not found!\n")


# see list of snacks sold
def view_sold_snacks():
    print("***** Sold Snacks *****")
    if len(soldSnacks) == 0:
        print("No snacks have been sold yet.\n")
    else:
        for item in soldSnacks:
            print(
                f"ID: {item['id']}\tName: {item['name']}\tPrice: {item['price']}")
        print()


# main function to continously shows options in cli
def inventory_management_app():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        print()

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_snack()
        elif choice == "3":
            update_snack()
        elif choice == "4":
            sell_snack()
        elif choice == "5":
            view_sold_snacks()
        elif choice == "6":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please try again.\n")


inventory_management_app()
