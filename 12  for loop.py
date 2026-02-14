# BASIC CODE 

for i in range(1, 16):
    print("GYAN BATRA ")

# even odd number 
 
for i in range(1, 51):
    if(i%2==0):
        print("enen number ",i)
    else:
        print("odd number",i)

# for loop table print 

for i in range(1, 11):
    x = 5 * i
    print("5 *", i, "=", x)

#printing numbers 1 to 'n'

a=int(input("enter the number: ="))
for i in range(1, a + 1):
    print("the number is = ",i)

# even numbers from 1 to 'n'

b=int(input("enter the number : = "))
for i in range (1 ,b + 1):
    if(i%2==0):
        print("even number ",i)

# count how many no. are divisible by 3 till n

c=int(input("enter the number : = "))
for i in range (1 ,c + 1):
    if(i%3==0):
        print("THE DIVISIBLE BY 3 ",i)

# the digit number it's once or tense 

digits  = int(input("Enter a number: "))
num = int(input("Enter the digit : = "))
print("You entered:", digits)
print("Total digits:", num)
for i in range (num):
    if(num==1):
        print("ITS ONCE DIGIT ")
    elif(num==2):
        print("ITS TENSE DIGIT ")
    elif(num==3):
        print("ITS HUNDRED DIGIT ")
    elif(num==4):
        print("ITS THOUSAND DIGIT ")
    elif(num==5):
        print("ITS TEN THOUSAND DIGIT ")
    elif(num==6):
        print("ITS LAKHS DIGIT")
    elif(num==7):
        print("ITS TEN LAKHS DIGIT ")
    else:
     print("too high 😱😱😱😱")  



n = int(input("Enter any number = "))
count = 0
temp = n

if n == 0:
    count = 1
else:
    for i in range(n):      # loop sirf control ke liye
        if temp > 0:
            temp = temp // 10
            count += 1
        else:
            break

print("Total digits =", count)

if count == 1:
    print("ITS ONCE DIGIT")
elif count == 2:
    print("ITS TENS DIGIT")
elif count == 3:
    print("ITS HUNDRED DIGIT")
elif count == 4:
    print("ITS THOUSAND DIGIT")
elif count == 5:
    print("ITS TEN THOUSAND DIGIT")
elif count == 6:
    print("ITS LAKHS DIGIT")
elif count == 7:
    print("ITS TEN LAKHS DIGIT")
else:
    print("too high 😱😱😱😱")


# leap year print

n=int(input("Enter The Year Number brom the ( Year : '2000' - Year : '2050') : = "))
for i in range(1):
    if(i%4==0 or i%100==0 or i%400==0) :
        print(n,"is a leap year")
    else:
        print(n,"its not a leap year ")


# count the character in name
text=input("enter your name")
count=0
for i in text:
    count=count+1
print("in your name chracter is : =  ",count)

# factorial of a number

num=int(input("enter any number: = "))
factorial=1
for i in range(1, num + 1):
    factorial=factorial*i
print("your factorial number is ",num,"=",factorial)

# palindrome check for loop 

n=int(input("enter the number"))
s=len(str(n))
temp = n
r=0

for i in range(s):
     q = n % 10
     r = r * 10 + q
     n = n // 10

if(temp==r):
        print("palindrome number")
else:
        print("not a palindrome number")
   



























































   
# palindrome check while loop 

n = int(input("enter the number: "))
temp = n
r = 0

while  n > 0:
    q = n % 10
    r = r * 10 + q
    n = n // 10

if temp == r:
    print("palindrome number")
else:
    print("not a palindrome number")


# fibonacci series for loop #
a = 0
b = 1
count=0
for i in range(1,13):
    print(a,end=" \n")
    c=a+b
    a=b
    b=c

# fibonacci series enteres by user 
n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1


import calendar
year=int(input("enter the year"))
month=int(input("enter the month"))

print("\n", calendar.month(year,month))