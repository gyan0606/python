print("Hello")
print("Welcome To Anaconda")
print("4")

num = int(input("Enter a number: "))
temp = num
count = 0

while temp > 0:
    temp = temp // 10
    count += 1

print("You entered:", num)

places = {
    1: "ONES",
    2: "TENS",
    3: "HUNDREDS",
    4: "THOUSANDS",
    5: "TEN THOUSANDS",
    6: "LAKHS",
    7: "TEN LAKHS",
    8: "CRORES"
}

if count in places:
    print(f"Your number is in {places[count]} place")
else:
    print("Your number is very very large 😮")
