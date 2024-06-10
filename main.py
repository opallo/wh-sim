from item import Item
import messages

inventory = []
days = 0

def show_menu():
  print(f"--> Day: {days}")
  print("0. Start Day")
  print("1. View Inventory")
  print("2. Add Item to Inventory")
  print("3. View Orders")
  print("4. Add Order")
  #print("\n")
  #print("Press 'q' to quit")
  
def show_inventory():
  
  if len(inventory) == 0:
    print("No items in warehouse")
  else:        
    for item in inventory:          
      print(f"Item: {item.name} Vendor: {item.vendor}")
  
def start_day():
  global days
  days += 1
  messages.loading_dots(f"Starting day {days}")

def main():
  print("\nWelome to Tiny Warehouse Simulator!")
  while True:   
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == 'q':
      break
    
    if choice == '0':
      start_day()
    
    elif choice == '1':
      messages.loading_dots("Checking inventory",10,3,0.5)
      show_inventory()
      
    elif choice == '2':
      print("Adding Item to Inventory...")
      
    elif choice == '3':
      print("Viewing Customer Orders")
      
    elif choice == '4':
      print("Adding Customer Order")
      
    input("Press Enter to continue...")
  
  
if __name__ == "__main__":
  main()
  
