# LMS SYSTEM OF COLLEGE 

name=(input("enter your name = "))
a=int(input("ener the roll. no 100 to 120 = "))
if(a>=100 and a<=120):
       print("your roll no is correct")
else:
       print("invalid roll no")

print("please select your department from below optons (1-5): \n ")
print("1. mechanical")
print("2. electronics & communication ")
print("3. computer science")
print("4. civil")
print("5. chemical")
b=int(input("enter the department  "))
print("Your department is",b)
if(b>=1 and b<=5):
    print("department is correct ")
else:
    print("not valid department !")


if(b==1):
       print("\n  you selected Mechanical \n ")
       print("1. your attendance")
       print("2. library status")
       print("3. calculate your percentage")
       c=int(input("please select from above questions = ") )
       if(c>=1 and c<=3):
            print("department is correct ")
            if(c==1):
                 print("you selected attendance \n ")
                 print("your attendance is 80 %")
            elif(c==2):
                 print("you selected library status ")
                 library=(input("all books given to library (Y/N)"))
                 if (library== "Y" or library== "y" ):
                      print("your library status is verified ")
                 else:
                      print("your library status is not verified !")
            elif(c==3):
                 print("you selected percentage section \n")
                 print("please enter your subject marks ( 5 )")
                 e=float(input("enter the marks of English = "))
                 h=float(input("enter the marks of Hindi = "))
                 g=float(input("enter the marks of Geography = "))
                 p=float(input("enter the marks of Psychology = "))
                 phy=float(input("enter the marks of Physical Education = "))
                 add=e+h+g+p+phy
                 percentage = (add/500)*100 
                 print("Total Marks = ", add)
                 print("Percentage = ", percentage)               
            else:
                 print("invalid !")
       else:
            print("not valid department !")
elif(b==2):
     print("you selected electronics & communication \n")
elif(b==3):
     print("you selected computer science")
elif(b==4):
     print("you selected civil")
elif(b==5):
     print("you selected chemical")
else:
    print("not valid !")