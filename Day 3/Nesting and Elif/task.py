#
#
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# print ("Welcome to amusement park")
# height= int(input("Enter your height in cm\n"))
#
# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("Enter your age\n"))
#     if age>=18:
#         print("Please pay $12")
#     else:
#         print("Please pay $7")
# else:
#     print("Sorry, you cannot ride the rollercoaster")

# if condition1:
#     do A
# elif condition2:
#     do B:
# else:
#     do this

print ("Welcome to amusement park")
height= int(input("Enter your height in cm\n"))

if height>=120 and height<=160:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age\n"))
    if age<12:
        print("Please pay $5")
    elif age>=12 and age<=18:
        print("Please pay $7")
    elif age>=18 and age<=24:
        print("Please pay $10")
    else:
        print("Please pay $12")
elif height>160:
    print("Sorry you are too tall")
else:
    print("Sorry, you cannot ride the rollercoaster")
