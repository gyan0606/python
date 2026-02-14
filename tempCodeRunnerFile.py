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