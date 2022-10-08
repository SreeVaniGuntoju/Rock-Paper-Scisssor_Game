#Rock,Paper,Scissor Game
import random
CHOICES=["rock","paper","scissor"]

while True:
    print("Lets play")
    user_choice=input("Type rock,paper,or scissor:")
    if user_choice in CHOICES :
        computer_choice=random.choice(CHOICES)
        print ("You threw "+ user_choice+" ,the computer threw "+computer_choice)
        # print (f"\you threw '{user_choice}',the computer threw '{computer_choice}'")
    else:
        print ("You typed "+ user_choice+" which isn't  a valid throw")
    again=input("\nWant some more??? (Y|N):")
    if again.lower()=="n":
        break
    print()
    
print("\nGoodbyee...")