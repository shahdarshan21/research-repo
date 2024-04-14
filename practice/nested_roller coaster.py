print("welcome to th roller coaster")
height = float(input("Let's measure your height (cm):"))
if height >= 120:
price = 0
print("child ticket are $5 \nYouth ticket are $7 \nAdult tickets are $12 \n")
age = int(input("How old are you? "))
if age < 12:
    price = 5
elif age <= 18:
    price = 7
else:
    price = 12
    photo_taken = input("Do you want a photo taken? Y or N ")
    if photo_taken.lower() == "Y":
        price += 3
        print(f"Your final bill is ${price}")
    else:
        print("You have to grow taller before you can take a ride")