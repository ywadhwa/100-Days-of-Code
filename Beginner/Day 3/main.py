ascii_art= """

***********************************************
         _________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
***********************************************
"""
print(ascii_art)
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()

if direction == "left":
    action = input("You come to a lake. There is an island in the middle of the lake.Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if door == "red":
            print("Burned by fire. Game over.")
        elif door == "yellow":
            print("You Win!")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over. ")
    elif action == "swim":
        print("Attacked by trout. Game over. ")

else:
    print("You have fallen into a hole. Game over.")

