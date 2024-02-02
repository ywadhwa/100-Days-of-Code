import os

print("Welcome to the secret auction program.")

auddict = {}
end_of_auction = False

def find_highest_bidder(auddict):
    highest = 0 
    winner = ""
    for bidder in auddict:
        bid_amt = auddict[bidder]
        if bid_amt > highest:
            highest = bid_amt
            winner  = bidder

    print(f"The winner is {winner} with a bid of {highest}")

while not end_of_auction:

    name = str(input("What is your name?: "))
    bid = int(input("What's your bid?: "))
    auddict[name] = bid

    Cont = input("Are there any other bidders? Type 'yes' or 'no'").lower()

    if Cont == "yes":
        os.system('cls')

    elif Cont == "no":
        find_highest_bidder(auddict)
        end_of_auction = True
