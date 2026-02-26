    # natural nu.till 50            ✅
    # odd even                      ✅
    # table by user                 ✅
    # reverse number 2208
    # sum of digit by user 
    # digit in line order 
    # largest nuber ,, smallest numer found
    # odd even or zero count        ✅
    # power code                    ✅
    # decimal to binary 
    # gcd of 2 number 


# natural nu.till 50
print("the all natural number till 50 are: ")
i=1
while(i<=50):
    print(i)
    i=i+1 

# odd even in while loop 
a=int(input("enter the number :"))
while(a>0):
    if(a % 2 == 0):
        print(a,"is even number")
    else:
        print(a,"is odd number")   

# table by user 
table=int(input(" enter the number till 100 for the table  " ))
if (table <=100 ):
    print("your table is:")
    i=1
    while(i<=10):
        x = table * i
        print(table,"x", i, "=", x)
        i=i+1
else:
    print("entered the value b/w  1 to 100 ")

# power code or sq root
sq=int(input("enter the number for sq root : "))
power=int(input("enter the power  : "))
result=1
i=1
while(i<=power):
 result=result*sq
 i =i+1
print("your answer of power is ",result)

# odd even or zero count
a=int(input("enter the number :"))
while(a>0):
    digit= a % 10
    if(digit % 2 == 0):
        print(digit,"is even number")
    else:
        print(digit,"is odd number")   
    a=a//10


num=int(input("enter any number: = "))
factorial=1
i=1
while (i<=num):
    factorial=factorial*i
    i=i+1
print("your factorial number is ",num,"=",factorial)