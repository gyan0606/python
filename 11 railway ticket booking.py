# # # INDIAN RAILWAY TICKET BOOKING

# # name=(input("enter the name : = " ))
# # print("Select the section b/w (1-2) ")
# # print("1.   ADULT AGE")
# # print("2.   TEENAGE")
# # age=int(input("Enter your Age for booking ticket : = \n"))
# # if(1>18 or 1<=100):
# #     print("YOUR CATEGORY IS ADULT ")
# # elif(2>=13 or 2<=18):
# #     print("YOUR CATEGORY IS TEENAGE " )
# # else:
# #     print("INVALID")

# # print("enter the coaches for the ticket booking  \n ")

# # print("1. general coach in this train is 4 \n 2 is in front \n 2 is in back ")
# # print("2. sleeper coach in this ain is ( s1 to s6  )  ")
# # print("3. coach second a/c (b1 to b6 )")
# # print("4. coach first a/c (a1 and a2 ) only ")
# # print("5. private cabin coach")
# # coaches=int(input("enter the coaches for the ticket booking  : = "))





# # Indian Railway Ticket Booking

# # Input passenger name
# name = input("Enter your name: ")

# # Display age category options
# print("Select the section b/w (1-2):")
# print("1. ADULT AGE")
# print("2. TEENAGE")

# # Input age for booking ticket
# age = int(input("Enter your Age for booking ticket: "))

# # Determine category based on age
# if age >= 18 and age <= 100:
#     print("YOUR CATEGORY IS ADULT")
# elif age >= 13 and age < 18:
#     print("YOUR CATEGORY IS TEENAGE")
# else:
#     print("INVALID AGE FOR BOOKING")

# # Display coach options
# print("\nEnter the coach for the ticket booking:")
# print("1. General coach in this train is 4 (2 in front, 2 in back)")
# print("2. Sleeper coach in this train is (S1 to S6)")
# print("3. Coach Second A/C (B1 to B6)")
# print("4. Coach First A/C (A1 and A2 only)")
# print("5. Private cabin coach (H1)")

# # Input coach choice
# coaches = int(input("Enter the coach number for the ticket booking: "))

# # Validate and print coach selection
# if coaches == 1:
#     print("You have selected General Coach.")
# elif coaches == 2:
#     print("You have selected Sleeper Coach.")
# elif coaches == 3:
#     print("You have selected Second A/C Coach.")
# elif coaches == 4:
#     print("You have selected First A/C Coach.")
# elif coaches == 5:
#     print("You have selected Private Cabin Coach.")
# else:
#     print("Invalid coach selection.")

# a=int(input("enter the journey in km : ="))
# print("the per km price is rs. 10/- ")

# pantry=(input("you have to need food in journey (y/n)"))
# if(pantry=="y or Y"):
#     print("menu or pantry car is : =")
#     print("chai               rs.10/-")
#     print("coffee             rs.30/-")
#     print("indian thali       rs.200/-")
#     print("vada pao           rs.50/-")
#     print("coldrink(can)      rs.60/-")
# else:
#     print("ok ! you did'nt need to food in journey \n")

# print("your pnr number is 427105708601\n")

# print(f"\nThank you {name} for booking your ticket with us.")

# Indian Railway Ticket Booking

name = input("Enter your name: ")

print("Select the section b/w (1-2):")
print("1. ADULT AGE")
print("2. TEENAGE")

age = int(input("Enter your Age for booking ticket: "))

if 18 <= age <= 100:
    print("YOUR CATEGORY IS ADULT")
elif 13 <= age < 18:
    print("YOUR CATEGORY IS TEENAGE")
else:
    print("INVALID AGE FOR BOOKING")
    
print("\nEnter the coach for the ticket booking:")
print("1. General coach (4 coaches)")
print("2. Sleeper coach (S1 to S6)")
print("3. Second A/C (B1 to B6)")
print("4. First A/C (A1 and A2)")
print("5. Private cabin coach (H1)")

coaches = int(input("Enter the coach number: "))

if coaches == 1:
    print("You have selected General Coach.")
elif coaches == 2:
    print("You have selected Sleeper Coach.")
elif coaches == 3:
    print("You have selected Second A/C Coach.")
elif coaches == 4:
    print("You have selected First A/C Coach.")
elif coaches == 5:
    print("You have selected Private Cabin Coach.")
else:
    print("Invalid coach selection.")
    exit()

distance = int(input("\nEnter the journey distance in km: "))
print("Per km price is Rs. 10/-")

base_fare = distance * 10
print(f"Base fare for {distance} km is Rs. {base_fare}/-")

total_fare = base_fare

pantry = input("\nDo you need food during the journey? (y/n): ").lower()

if pantry == "y":
    print("\nMenu in pantry car:")
    print("1. Chai               Rs. 10/-")
    print("2. Coffee             Rs. 30/-")
    print("3. Indian Thali       Rs. 200/-")
    print("4. Vada Pao           Rs. 50/-")
    print("5. Coldrink (can)     Rs. 60/-")

    food_choice = input("Enter food item number (or press Enter to skip): ")

    food_prices = {
        "1": 10,
        "2": 30,
        "3": 200,
        "4": 50,
        "5": 60
    }

    if food_choice in food_prices:
        food_cost = food_prices[food_choice]
        total_fare += food_cost
        print(f"Food cost Rs. {food_cost}/- added.")
    elif food_choice != "":
        print("Invalid food choice, no food added.")
else:
    print("No food selected.")

pnr_number = "427105708601"
print(f"\nYour PNR number is {pnr_number}")

print(f"\nThank you {name} for booking your ticket with us.")
print(f"Total amount to be paid: Rs. {total_fare}/-")
