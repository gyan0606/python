# age voting code 
age = int(input("enter your age"))
if(age<18):
    print("you can't vote")
elif(age>100):
    print("invalid age !")
else:
    print("you are eligible for vote")
    

# odd even code 
num=int(input("enter a number"))
if(num%2==0):
    print("even number ")
else:
    print("odd number")


# negative , positive or zero 0 
a=int(input("enter the number"))
if(a>0):                     
    print("you entered positive number = ",a)
elif(a<0):
    print("you entered negative number = ",a)  
else:                              # a==0 print("you entered zero number")
    print("you entered zero number = ",a)
 

# which number is greater  
num1=int(input("enter the first number="))
num2=int(input("enter the second number="))
num3=int(input("enter the third number=" ))
if(num1>num2 and num1>num3):                    # && operator (and) 
    print("number first is greater")
elif(num2>num1 and num2>num3):
    print("number second is greater")
elif(num3>num1 and num3>num2):
    print("number third is greater")
else:
    print("number are equal greater ")


#cars booking 
cars=(input("enter the car"))
cars = ["Innova Crysta", "Kia Carens", "Ertiga"]
cars = "Kia Carens" 
if cars in cars: 
    print(f"{cars} is available.")
else:
    print(f"{cars} is not available.")


# marks grading system
e=float(input("enter the marks of English = "))
h=float(input("enter the marks of Hindi = "))
g=float(input("enter the marks of Geography = "))
p=float(input("enter the marks of Psychology = "))
phy=float(input("enter the marks of Physical Education = "))
add=e+h+g+p+phy
percentage = (add/500)*100 
print("Total Marks = ", add)
print("Percentage = ", percentage)
if(percentage >= 91 and percentage <= 100):
    print("A1")
elif(percentage >= 81 and percentage <= 90):
    print("A2")
elif(percentage >= 71 and percentage <= 80):
    print("B1")
elif( percentage >= 61 and percentage <= 70):
    print("B2")
elif(percentage >= 51 and percentage <= 60):
    print("c1")
elif(percentage >= 41 and percentage <= 50):
    print("C2")
elif(percentage<33):
    print("fail")
else:
    print("indicates a need for improvement")
