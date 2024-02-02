import game_data
import random
import art

game_over = False

compA = random.randint(1,50)
compB = random.randint(1,50)

count = 0 

def compare(compA,compB):
        if game_data.data[compA]['follower_count'] > game_data.data[compB]['follower_count']:
            return "A"
        else:
            return "B"

while not game_over:


    print(art.logo)
    A_dict = game_data.data[compA]
    print(f"Compare A: {A_dict['name']}, a {A_dict['description']}, from {A_dict['country']}.") 

    print(art.vs)

    B_dict = game_data.data[compB]
    print(f"Against B: {B_dict['name']}, a {B_dict['description']}, from {B_dict['country']}.") 

    answer = compare(compA,compB).lower()

    followinput = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == followinput:
        count = count + 1
        print(f"You are correct. Your score is {count}")
        
        if answer == 'a':
            compB = random.randint(1,50)
        elif answer == 'b':
             compA = compB
             compB = random.randint(1,50)    
        
    else:
        print(f"You lose. Your final score is {count}")
        game_over = True

