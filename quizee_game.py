print("Welcome to my quize game!")

playing = input("Do u want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :")
score=0

answer = input("what does cpu stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!") 

answer = input("What does ram stand for? ")
if answer.lower() == "random acess memory":
    print('correct!')
    score += 1
else:
    print("Icorrect!")

answer = input("What does Gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Icorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('correct!')
    score += 1
else:
    print("Icorrect!")

print("You got" + str(score) + "questions correct!")
print("YOU got " + str((score / 4) * 100) + "%.")

