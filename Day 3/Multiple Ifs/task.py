print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Child ticket price $5.")
    elif age <= 18:
        bill=7
        print("Teenager ticket price is $7.")
    else:
        bill=12
        print("Adult ticket price is $12.")
    photo_consent=input("Do you want any photos? (y/n)")
    if photo_consent=="y":
        bill += 3
    else:
        print(f"Your bill is ${bill}")

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
