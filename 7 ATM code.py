# # ATM machine code
# balance=50000
# pin=int(input("enter the pin"))
# if(pin==8601):
#     print("your pin is correct ")
#     print("1. View Balance\n")
#     print("2. Withdraw Money\n")
#     print("3. Deposit Money\n")
#     print("4. Mini Statement\n")
#     print("5. Fund Transfer\n")
# choice=(input("enter your choice "))
# if(choice==1):
#     print("your balance is",balance)
# elif(choice==2):
#     amount=int(input("withdrawn amount"))
#     if(amount<=balance):
#         balance=balance-amount
#         print("please collect your cash ")
#         print("remaining balance",balance)
# else:
#     print("insufficent balance ")
# elif(choice==3):
# amount=int(input("enter the aount of deposit"))
# balance=balance+amount
# print("your amount deposit successfully")
# print("updated balance",balance)
# elif(choice==4):
# old_pin=input("enter the old pin :")
# if(old_pin==pin):
#     pin=input("enter the new pin")
#     print("pin changed successfully")
# else:
#     print("wrong pin")
# elif(choice==5):
# acc_no=input("enter the receiver account number")
# amount=int(input("enter the amount of transfer"))
# if(amount<=balance):
# balance=balance-amount
# print("amounttransferred successfully")
# print("remaining balance",balance)
# else:
# print("insufficent balance")
# else:
# print("invalid choice")
# else:
#     print("your pin is incorrect ! ")

balance = 50000

pin = int(input("Enter the pin: "))

if (pin == 8601):
    print("Your pin is correct")
    print("1. View Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Mini Statement")
    print("5. Fund Transfer")

    choice = int(input("Enter your choice: "))

    if (choice == 1):
        print("Your balance is", balance)

    elif( choice == 2):
        amount = int(input("Withdraw amount: "))
        if (amount <= balance):
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif (choice == 3):
        amount = int(input("Enter the amount to deposit: "))
        balance = balance + amount
        print("Your amount deposited successfully")
        print("Updated balance:", balance)

    elif (choice == 4):
        old_pin = int(input("Enter the old pin: "))
        if (old_pin == pin):
            pin = int(input("Enter the new pin: "))
            print("Pin changed successfully")
        else:
            print("Wrong pin")

    elif( choice == 5):
        acc_no = input("Enter the receiver account number: ")
        amount = int(input("Enter the amount to transfer: "))
        if (amount <= balance):
            balance = balance - amount
            print("Amount transferred successfully")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    else:
        print("Invalid choice")

else:
    print("Your pin is incorrect!")




from datetime import datetime

print("\n" + "="*60)
print("        🌟 THE ROYAL ORCHID – 5 STAR DINING 🌟")
print("="*60)
print("Address : Luxury Avenue, City Center")
print("Contact : +91-98765-43210")
print("-"*60)

now = datetime.now()
print(f"Date : {now.strftime('%d-%m-%Y')}    Time : {now.strftime('%I:%M %p')}")
print("Table No : 12        Bill No : 4587")
print("-"*60)

category = input("Select Category (VEG / NON): ").upper()

total = 0
items = []

if category == "VEG":
    sub = input("Select (D = Drinks / F = Food): ").upper()

    if sub == "D":
        menu = {
            "Fresh Lime Soda": 120,
            "Cold Coffee": 180,
            "Green Tea": 150,
            "Mint Mojito": 220,
            "Fruit Punch": 250
        }
    else:
        menu = {
            "Paneer Butter Masala": 420,
            "Veg Biryani": 380,
            "Stuffed Naan": 120,
            "Mediterranean Salad": 300,
            "Cheese Platter": 450
        }

else:
    menu = {
        "Chicken Biryani": 520,
        "Butter Chicken": 620,
        "Grilled Fish": 750,
        "Chicken Steak": 680,
        "Egg Curry": 360
    }

print("\n--------- MENU ---------")
for i, p in menu.items():
    print(f"{i:30} ₹{p}")

print("\nEnter quantity (0 if not ordered)\n")

for item, price in menu.items():
    qty = int(input(f"{item}: "))
    if qty > 0:
        amount = qty * price
        total += amount
        items.append((item, qty, amount))

# TAX
service_tax = total * 0.05
gst = total * 0.12
grand_total = total + service_tax + gst

# BILL
print("\n" + "="*60)
print("                 🧾 TAX INVOICE")
print("="*60)
print(f"{'ITEM':30}{'QTY':>6}{'AMOUNT':>12}")
print("-"*60)

for i, q, a in items:
    print(f"{i:30}{q:>6} ₹{a:>9}")

print("-"*60)
print(f"{'Sub Total':38} ₹{total:>9}")
print(f"{'Service Charge (5%)':38} ₹{service_tax:>9.2f}")
print(f"{'GST (12%)':38} ₹{gst:>9.2f}")
print("-"*60)
print(f"{'GRAND TOTAL':38} ₹{grand_total:>9.2f}")
print("="*60)
print("   Thank You for Dining with THE ROYAL ORCHID")
print("        We Hope to Serve You Again 🌸")
