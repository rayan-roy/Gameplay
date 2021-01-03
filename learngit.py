hungry = input("Are you hungry ")
if hungry == "yes":
    print("Eat some food")
    print("Drink some water")
elif hungry == "maybe":
    print("decide one")
else:
    thirsty = input("Are you thirsty ")
    if thirsty == "yes":
        print("drink water")