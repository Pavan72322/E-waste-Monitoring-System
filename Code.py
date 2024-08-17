from datetime import datetime
from dateutil.relativedelta import relativedelta

class E_WasteItem:
    def __init__(self, name, purchase_date, lifespan_years):
        self.name = name
        self.purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        self.lifespan_years = lifespan_years
        self.expiry_date = self.purchase_date + relativedelta(years=lifespan_years)

    def check_status(self):
        today = datetime.now()
        if today >= self.expiry_date:
            return f"{self.name} is due for recycling."
        else:
            return f"{self.name} is still in use."

items = []
while True:
    print("\n--- E-waste Monitoring System ---")
    print("1. Add Electronic Item")
    print("2. Check Item Status")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter item name: ")
        purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
        lifespan_years = int(input("Enter expected lifespan (years): "))
        try:
            item = E_WasteItem(name, purchase_date, lifespan_years)
            items.append(item)
            print(f"{name} added successfully!")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    elif choice == '2':
        if items:
            for item in items:
                print(item.check_status())
        else:
            print("No items to check.")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
