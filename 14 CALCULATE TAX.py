# tax calculation code 
print("=== Vehicle Toll Tax Calculator === \n")

print("CHANDIGARH  toll tax price is fixed =  RS. 200/- \n")
fixed_amount = 200

print(" 1. Two wheeler (like: = Bike , activa , sports bike  \n")
print(" 2. Four wheeler (like: = car , jeep , tempo traveller , ,bus , small truck etc.)\n")
print(" 3. heavy vehicles : = heavy loaded trucks , etc \n")
a=int(input("enter your vehicle type from below options : = "))
if(a==1):
    print("you selected  Two wheeler (like: = Bike , activa , sports bike \n")
    cc = int(input("Enter engine capacity (cc): "))

    if (cc <= 150):
        tax_percent = 5
    else:
        tax_percent = 7

elif(a==2):
    print(" you selected Four wheeler (like: = car , jeep , tempo traveller , ,bus , small truck etc.\n)")
    cc = int(input("Enter engine capacity (cc): "))

    if (cc <= 1000):
        tax_percent = 8
    elif (cc <= 2000):
        tax_percent = 10
    else:
        tax_percent = 12

elif(a==3):
    print(" heavy vehicles : = heavy loaded trucks , etc")
    cc = int(input("Enter engine capacity (cc): "))
    tax_percent = 15
else:
    print("Invalid vehicle type!")
    exit()

tax_amount = (tax_percent / 100) * fixed_amount
total_amount = fixed_amount + tax_amount

print("\n===== BILL =====")
print(f"Vehicle Type: {a}")
print(f"Base Toll Amount: ${fixed_amount}")
print(f"Tax ({tax_percent}%): ${tax_amount}")
print(f"Total Payable Amount: ${total_amount}")

