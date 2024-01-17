import random
import os

def play_game():

    play_blackjack = True

    user_card = []
    comp_card = []

    for i in range(2):
        user_card.append(random.randint(1,11))
        comp_card.append(random.randint(1,11))

    while play_blackjack:
        user_sum = calculate_score(user_card)
        comp_sum = calculate_score(comp_card)  

        print(f"You cards: {user_card}")
        print(f"Computer's first hand: {comp_card[0]} ")

        if user_sum == 0 or comp_sum == 0 or user_sum > 21:
            is_game_over = True
        
        else:

            cont = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if cont == "y":
                user_card.append(random.randint(1,11))

            elif cont == "n":
                play_blackjack = False

    while comp_sum != 0 and comp_sum < 17:
        comp_card.append(random.randint(1,11))
        comp_sum = calculate_score(comp_card) 

    print(f"Your final hand: {user_card}, final score: {user_sum}")
    print(f"Computer's final hand: {comp_card}, final score: {comp_sum}")
    print(compare(user_sum, comp_sum))

def compare(user_sum,comp_sum):

    if user_sum > comp_sum:
        return "You Win "
    
    elif user_sum == comp_sum:
        return "Draw"
    
    elif user_sum > 21:
        return "You went over. You lose."
    
    elif comp_sum > 21:
        return "Opponent went over. You win."
    
    elif user_sum == 0:
        return "Win with a blackjack."
    
    elif comp_sum == 0:
        return "Lose, opponent has blackjack."

    elif user_sum < comp_sum:
        return "You Lose"

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


while input("Do you want to play a game of Blackjack? Type 'yes' or 'no':") == 'yes':
    os.system('cls')
    play_game()
    