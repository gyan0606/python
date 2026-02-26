print("\t\t\t\t WELCOME TO THE GYAN HOTEL")
category=(input("veg/nonveg =   "))
if(category=="veg" or "VEG"):
    items=input(("Select (d = Drinks / f = Food): "))
    if(items=="d"):
            print("Fresh Lime Soda            : 120")
            print("Cold Coffee                : 180")
            print("Green Tea                  : 150")
            print("Mint Mojito                : 220")
            print("Fruit Punch                : 250")

            a=int(input("Fresh Lime Soda qty = "))
            b=int(input("Cold Coffee qty = "))
            c=int(input("Green Tea qty = "))
            d=int(input("Mint Mojito qty = "))
            e=int(input("Fruit Punch qty = "))
            total = a*120 + b*180 + c*150 + d*220 + e*250    
    else:
            print("Paneer Butter Masala      : 420")
            print("Veg Biryani               : 380")
            print("Stuffed Naan              : 120")
            print("Mediterranean Salad       : 300")
            print("Cheese Platter            : 450") 

            q1 = int(input("Paneer Butter Masala qty = "))
            q2 = int(input("Veg Biryani qty = "))
            q3 = int(input("Stuffed Naan qty = "))
            q4 = int(input("Mediterranean Salad qty = "))
            q5 = int(input("Cheese Platter qty = "))
            total = q1*420 + q2*380 + q3*120 + q4*300 + q5*450

else:
        print("chicken biryani       : 350")
        print("tandori chicken       : 500")
        print("butter chicken        : 450")
        print("butter lemon chicken  : 450")
        print("chicken tikka         : 500")

        q1 = int(input("Chicken Biryani qty = "))
        q2 = int(input("Tandoori Chicken qty = "))
        q3 = int(input("Butter Chicken qty = "))
        q4 = int(input("Butter Lemon Chicken qty = "))
        q5 = int(input("Chicken Tikka qty = "))

        total = q1*350 + q2*500 + q3*450 + q4*450 + q5*500

# ---------------- BILL ----------------
print("\n\t\tGYAN HOTEL BILL")
print("-------------------------------")
print("Total Amount = ₹", total)
print("Thank You! Visit Again  ")

print("\n enter the quantity (if 0 the item in not) ")
