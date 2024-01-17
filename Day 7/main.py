stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




word = str(input("Enter a word of you choice: \n"))

display = []

for d in range(len(word)):
    display.append("_")

print("***********Hangman Game***********")


no_of_lives = 6

while "_" in display:

    guess_letter = str(input("Enter a letter. \n")).lower()

    for i in range(len(word)):
        letter = word[i]
        
        if letter == guess_letter:
            display[i] = letter

    if guess_letter not in word:
        no_of_lives = no_of_lives - 1
        if no_of_lives == 0:
            print("You lose.")   

    if "_" not in display:
        print("You Win.")

print(stages[no_of_lives])