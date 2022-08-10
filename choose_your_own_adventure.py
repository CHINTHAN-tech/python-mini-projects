name = input("Type your name: ")
print("Welcome", name, "to this game!")

answer = input(
    "you are on a dirt road, it has come to an end and you can go left or right. which way would you go? ").lower()

if answer == "left":
    answer = input(
        "you come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("YOu swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. you loose.')

elif answer == "right":
    answer = input(
        "you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    
    if answer == "back":
        print("YOU go back and loose.")
    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
           

        if answer == "yes":
            print("YOU talk to the stranger and they give you gold. you WIN!")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you loose.")
        else:
            print('NOt a valid option. you loose.')
    else:
        print("NOY a valid option. you lose.")

else:
    print("Not a valid option. you lose.")

print("Thank you for trying", name)
    