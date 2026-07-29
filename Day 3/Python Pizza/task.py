print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
#the submission is correct it's just that it does not matches with the exact code of Angela
bill=0

# if size=="S":
#     bill+=15
#     print(f"Your final bill is ${bill}")
#     if pepperoni=="Y":
#         bill += 2
#         print(f"Your final bill is ${bill}")
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Your final bill is ${bill}")
#     else:
#         print(f"Your final bill is ${bill}")
#
# elif size=="M":
#     bill+=20
#     print(f"Your final bill is ${bill}")
#     if pepperoni == "Y":
#         bill += 3
#         print(f"Your final bill is ${bill}")
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Your final bill is ${bill}")
#     else:
#         print(f"Your final bill is ${bill}")
#
# elif size=="L":
#     bill+=25
#     print(f"Your final bill is ${bill}")
#     if pepperoni == "Y":
#         bill += 3
#         print(f"Your final bill is ${bill}")
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Your final bill is ${bill}")
#     else:
#         print(f"Your final bill is ${bill}")
#
# else:
#     print("You typed the wrong inputs")
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Sorry, please enter S, M, or L")
    exit()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    bill+=1
print(f"Your final bill is: ${bill}.")