# for loop
s=input("Enter any no.= ")
count=0

for ch in s:
    count=count+1
    
print (count)
if(count==1):
        print("ITS ONCE DIGIT ")
elif(count==2):
        print("ITS TENSE DIGIT ")
elif(count==3):
        print("ITS HUNDRED DIGIT ")
elif(count==4):
        print("ITS THOUSAND DIGIT ")
elif(count==5):
        print("ITS TEN THOUSAND DIGIT ")
elif(count==6):
        print("ITS LAKHS DIGIT")
elif(count==7):
        print("ITS TEN LAKHS DIGIT ")
else:
     print("too high 😱😱😱😱") 


# with the for loop and with condition 
n=int(input("Enter any number = "))
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


#adition of d/f odd num and even number
a=int(input("enter the first number"))
b=int(input("enter the second number"))

even_sum=0
odd_sum=0
for i in range(1):
    if a % 2 == 0:
        even_sum += a
    else:
        odd_sum += a
    if b % 2 == 0:
         even_sum += b
    else:
         odd_sum += b

print("Sum of EVEN digits =",even_sum)
print("Sum of ODD digits  =",odd_sum)



# add of odd / even from 50 numbers 

n=int(input("Enter value of n = "))
even_sum=0
odd_sum=0
for i in range(1,n+1):
    if i % 2 == 0:
        even_sum = even_sum + i
        odd_sum =  odd_sum + i
        print("sum of even no : = ",even_sum)
        print("sum of odd number: = ",odd_sum)
 
        
n = int(input("Enter value of n = "))
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)



#PATTERN FOR LOOP  1 to 5

for i in range(1,6):
     print("& " * i)

#pattern  reverse 5 to 1 
for i in range(5,0,-1):
     print("& " * i)


#other pattern for loop triangle 9 to 1 
for i in range(1,6):
     print("& " * i)   
for i in range(4,0,-1):
     print("& " * i)



 # pattern  pyramid
rows = 5
#  upper pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# lower pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()




# pattern triangle
n = 5
# upper part
for i in range(1, n + 1):
    print(" " * (2 * (n - 1)) + "*  " * i)
# lower part
for i in range(n - 1, 0, -1):
    print(" " * (2 * (n - 1)) + "*  " * i)



# pattern    straight triangle
rows = 5
for i in range(1, rows + 1):
    # spaces
    print(" " * (rows - i), end="")
    # stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()

