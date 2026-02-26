def factorial(num):
    a=int(input("enter the number : "))
    fact=1
    for i in range(1,a+1):
        fact*=i
        i+=1
        print("your factorial number is ",num)