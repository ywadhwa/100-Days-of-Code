#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

with open(os.getcwd() + "/Input/Letters/starting_letter.txt","r") as sample_letter:
    letter_content = sample_letter.read()

name_list = []
with open(os.getcwd() + "/Input/Names/invited_names.txt") as name:
    for i in name:
        stripped_names = i.rstrip("\n")
        name_list.append(stripped_names)

for name in name_list:
    with open(os.getcwd() + f"/Output/ReadyToSend/letter_for_{name}.txt","w") as output:
        replace_text = letter_content.replace("[name]", name)
        output.write(replace_text)



