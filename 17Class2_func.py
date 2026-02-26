# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))

elif choice == 2:
    print("Result =", subtract(num1, num2))

elif choice == 3:
    print("Result =", multiply(num1, num2))

elif choice == 4:
    print("Result =", divide(num1, num2))

else:
    print("Invalid Choice")



def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        i=i+1

    return fact

a=int(input("enter the number : "))
print("your factorial number is ",factorial(a))


def odd(even):
    if (a%2==0):
        return "even"
    else:
        return "odd"

        
a=int(input("enter the number : "))
print("your number is ",odd(a))

       
def add (a,b,plus=0):
    x=a+b+plus
    return x
c= add (10,45)
print (c)
d=add (10,45,20)
print (d)


# lambda function
square =lambda x:x*x
print(square(3))

#  sum lambda
sum =lambda x,y :x+y
print(sum(3,5))