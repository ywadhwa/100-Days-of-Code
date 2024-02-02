import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]


userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print(images[userinput])

if userinput not in [0,1,2]:
    print("Wrong Input!!!")
    sys.exit()


compinput = random.randint(0,2)
print("Computer Choice:")
print(images[compinput])

if userinput == compinput:
    print("Draw")
elif userinput == 0 and compinput == 1:
    print("You Lose.")
elif userinput == 0 and compinput == 2:
    print("You Win.")
elif userinput == 1 and compinput == 0:
    print("You Win.")
elif userinput == 1 and compinput == 2:
    print("You Lose.")
elif userinput == 2 and compinput == 0:
    print("You Lose.")
elif userinput == 2 and compinput == 1:
    print("You Win.")