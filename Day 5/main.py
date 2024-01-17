import string
import random

print("Welcome to the PyPassword Generator!")
pinput = int(input("How many letters would you like in your password? \n"))
syms = int(input("How many symbols would you like? \n"))
number = int(input("How many numbers would you like? \n"))

llist = []

for i in range(pinput):
    llist.append(random.choice(string.ascii_letters))

for j in range(syms):
    llist.append(random.choice(string.punctuation))

for k in range(number):
    llist.append(str(random.randint(0,9)))

random.shuffle(llist)

password = "".join(llist)
print(f"You password is:{password}")