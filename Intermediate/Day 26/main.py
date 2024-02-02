import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato = pd.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for index,row in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_code():

    user_input = input("Enter a word: ")

    try:
        phonetic = [new_dict[x.upper()] for x in user_input]
    except KeyError:
        print("Only letters.")
        generate_code()
    else:
        print(phonetic)

generate_code()