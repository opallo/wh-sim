from item import Item
import messages
from database import create_table

days = 0

def show_menu():
    print(f"--> Day: {days}")
    print("0. Start Day")
    print("1. View Inventory")
    print("2. Add Item to Inventory")
    print("3. View Orders")
    print("4. Add Order")
    print("Press 'q' to quit")

def show_inventory():
    items = Item.fetch_all()
    if not items:
        print("No items in warehouse")
    else:
        for item in items:
            print(f"Item: {item[1]} Vendor: {item[5]}")
def start_day():
    global days
    days += 1
    messages.loading_dots(f"Starting day {days}")
    print(f"Day {days} complete!")

def add_item():
    name = input("Enter item name: ")
    barcode = input("Enter barcode: ")
    size = input("Enter size: ")
    weight = input("Enter weight: ")
    vendor = input("Enter vendor: ")
    item = Item(name, barcode, size, weight, vendor)
    item.save_to_db()
    print(f"Added item: {name}")

def main():
    create_table()
    print("\nWelcome to Tiny Warehouse Simulator!")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == 'q':
            break
        
        if choice == '0':
            start_day()
        
        elif choice == '1':
            messages.loading_dots("Checking inventory", 3, 3, 0.5)
            show_inventory()
        
        elif choice == '2':
            add_item()
        
        elif choice == '3':
            print("Viewing Customer Orders")
        
        elif choice == '4':
            print("Adding Customer Order")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
