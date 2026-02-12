# TICKET BOOKING

a=(input("enter the name " ))
print("Select the section b/w (1-2) ")
print("1.   ADULT AGE")
print("2.   TEENAGE")
c=int(input("Enter your Age for booking ticket \n"))
if(1>18 or 1<=100):
    print("YOUR CATEGORY IS ADULT ")
elif(2>=13 or 2<=18):
    print("YOUR CATEGORY IS TEENAGE " )
else:
    print("INVALID")

b=int(input(" select the airline from the below options: \n 1. INDIGO \n 2. BRITISH AIRWAYS \n 3. AMERICAN AIRLINES \n 4. AIR NEW ZEALAND \n 5. EMIRATES "))
if(b==1):
    print("YOUR AIRLINE IS INDIGO")
elif(b==2):
    print("YOUR AIRLINE BRITISH AIRWAYS")
elif(b==3):
    print("YOUR AIRLINE AMERICAN AIRLINES")
elif(b==4):
    print("YOUR AIRLINE AIR NEW ZEALAND")
elif(b==5):
    print("YOUR AIRLINE EMIRATES")
else:
    print("invalid airlines ")

print("enter the journey details below:")
e=input("enter the DEPARTURE LOCATION = ")
f=input("enter the ARRIVAL LOCATION = ")



print("\nChoose your travel section:")
print("1. Economy")
print("2. Business")
print("3. Premium")

section = input("Enter your choice (1/2/3): ")

# Default ticket prices
if section == "1":
    adult_price = 20000
    child_seat_price = 14000
    child_lap_price = 0
    teen_price = 16000
    section_name = "Economy"

elif section == "2":
    adult_price = 40000
    child_seat_price = 28000
    child_lap_price = 0
    teen_price = 30000
    section_name = "Business"

elif section == "3":
    adult_price = 60000
    child_seat_price = 42000
    child_lap_price = 0
    teen_price = 45000
    section_name = "Premium"

else:
    print("Invalid choice! Defaulting to Economy.")
    adult_price = 20000
    child_seat_price = 14000
    child_lap_price = 0
    teen_price = 16000
    section_name = "Economy"

print(f"\nTicket Prices for {section_name} Section:")
print("Adult Ticket Price =", adult_price)
print("Child (Seat) Ticket Price =", child_seat_price)
print("Child (Lap) Ticket Price =", child_lap_price)
print("Teenager Ticket Price =", teen_price)


print("\nSelect the section b/w (1-3) FOR CONFIRMING THE TICKET")
print("1. ADULT PASSENGERS ")
print("2. CHILD (INFANT ON SEAT) PASSENGERS")
print("3. CHILD (INFANT IN LAP) PASSENGERS")
print("4. TEENAGE PASSENGERS")

age1 = int(input("Enter the ADULT passengers: "))
age2 = int(input("Enter the CHILD (INFANT ON SEAT) passengers: "))
age3 = int(input("Enter the CHILD (INFANT IN LAP) passengers: "))
age4 = int(input("Enter the TEENAGE passengers: "))

total_passengers = age1 + age2 + age3 + age4
print("Total passengers:", total_passengers)

# Luggage rules
print("\nCHECK-IN LUGGAGE LIMIT = 7 KG")
print("BAGGAGE LIMIT = 30 KG")
print("If you cross the limit, fine = Rs. 1000 per kg")
print("MAX LIMIT: CHECK-IN = 10 KG, BAGGAGE = 40 KG")

check_in_weight = int(input("Enter CHECK-IN luggage weight (kg): "))
baggage_weight = int(input("Enter BAGGAGE weight (kg): "))

# Fine calculation
fine = 0
if check_in_weight > 7:
    excess = check_in_weight - 7
    fine += excess * 1000
if baggage_weight > 30:
    excess = baggage_weight - 30
    fine += excess * 1000

# Total bill calculation
total_bill = (age1 * adult_price) + (age2 * child_seat_price) + (age3 * child_lap_price) + (age4 * teen_price) + fine

# Final summary
print("\n----- BOOKING SUMMARY -----")
print("Passenger Name:",a)
print("Airline:", b)
print("From:", e, "To:", f)
print("Travel Section:", section_name)
print("Total Passengers:", total_passengers)
print("Ticket Cost (without fine):", (age1 * adult_price) + (age2 * child_seat_price) + (age3 * child_lap_price) + (age4 * teen_price))
print("Fine for excess luggage:", fine)
print("TOTAL BILL =", total_bill)
print("---------------------------")









# TICKET BOOKING SYSTEM

# Passenger name
name = input("Enter the name: ")

# Age category check
age = int(input("Enter your Age for booking ticket: "))
if age >= 18 and age <= 100:
    print("YOUR CATEGORY IS ADULT")
elif age >= 13 and age < 18:
    print("YOUR CATEGORY IS TEENAGE")
else:
    print("INVALID AGE CATEGORY")

# Airline selection
print("\nSelect the airline from the below options:")
print("1. INDIGO")
print("2. BRITISH AIRWAYS")
print("3. AMERICAN AIRLINES")
print("4. AIR NEW ZEALAND")
print("5. EMIRATES")

b = int(input("Enter your choice (1-5): "))
if b == 1:
    airline = "INDIGO"
elif b == 2:
    airline = "BRITISH AIRWAYS"
elif b == 3:
    airline = "AMERICAN AIRLINES"
elif b == 4:
    airline = "AIR NEW ZEALAND"
elif b == 5:
    airline = "EMIRATES"
else:
    airline = "INVALID AIRLINE"

print("Your airline is:", airline)

# Journey details
departure = input("Enter the DEPARTURE LOCATION = ")
arrival = input("Enter the ARRIVAL LOCATION = ")

# Travel section
print("\nChoose your travel section:")
print("1. Economy")
print("2. Business")
print("3. Premium")

section = input("Enter your choice (1/2/3): ")

# Default ticket prices
if section == "1":
    adult_price = 20000
    child_seat_price = 15000
    child_lap_price = 0
    teen_price = 14000
    section_name = "Economy"

elif section == "2":
    adult_price = 40000
    child_seat_price = 30000
    child_lap_price = 0
    teen_price = 28000
    section_name = "Business"

elif section == "3":
    adult_price = 60000
    child_seat_price = 45000
    child_lap_price = 0
    teen_price = 42000
    section_name = "Premium"

else:
    print("Invalid choice! Defaulting to Economy.")
    adult_price = 20000
    child_seat_price = 15000
    child_lap_price = 0
    teen_price = 14000
    section_name = "Economy"

print(f"\nTicket Prices for {section_name} Section:")
print("Adult Ticket Price =", adult_price)
print("Child (Seat) Ticket Price =", child_seat_price)
print("Child (Lap) Ticket Price =", child_lap_price)
print("Teenager Ticket Price =", teen_price)

# Passenger counts
print("\nEnter passenger details:")
age1 = int(input("Enter the ADULT passengers: "))
age2 = int(input("Enter the CHILD (INFANT ON SEAT) passengers: "))
age3 = int(input("Enter the CHILD (INFANT IN LAP) passengers: "))
age4 = int(input("Enter the TEENAGE passengers: "))

total_passengers = age1 + age2 + age3 + age4
print("Total passengers:", total_passengers)

# Luggage rules
print("\nCHECK-IN LUGGAGE LIMIT = 7 KG")
print("BAGGAGE LIMIT = 30 KG")
print("If you cross the limit, fine = Rs. 1000 per kg")
print("MAX LIMIT: CHECK-IN = 10 KG, BAGGAGE = 40 KG")

check_in_weight = int(input("Enter CHECK-IN luggage weight (kg): "))
baggage_weight = int(input("Enter BAGGAGE weight (kg): "))

# Fine calculation
fine = 0
if check_in_weight > 7:
    excess = check_in_weight - 7
    fine += excess * 1000
if baggage_weight > 30:
    excess = baggage_weight - 30
    fine += excess * 1000

# Total bill calculation
total_bill = (age1 * adult_price) + (age2 * child_seat_price) + (age3 * child_lap_price) + (age4 * teen_price) + fine

# Final summary
print("\n----- BOOKING SUMMARY -----")
print("Passenger Name:", name)
print("Airline:", airline)
print("From:", departure, "To:", arrival)
print("Travel Section:", section_name)
print("Total Passengers:", total_passengers)
print("Ticket Cost (without fine):", (age1 * adult_price) + (age2 * child_seat_price) + (age3 * child_lap_price) + (age4 * teen_price))
print("Fine for excess luggage:", fine)
print("TOTAL BILL =", total_bill)
print("---------------------------")