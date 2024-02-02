print("Welcome to the tip calculator")
bamnt = float(input("What was the total bill? $"))
ppl = int(input("How many people to split the bill?"))
tip = int(input("What % tip would you like to give? 10,12 or 15?"))
payment = (bamnt + bamnt * tip/100 ) / ppl

print(f"Each person should pay: {payment:.2f}")