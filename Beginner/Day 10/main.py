import os

def operation (n1, n2, ops):

    if ops == "+":
      return n1 + n2
    elif ops == "-":
      return n1 - n2
    elif ops == "*":
      return n1 * n2
    elif ops == "/":
      return n1 / n2


def calculator():

    n1 = int(input("Enter the first number: "))

    op_list = ["+","-","*","/"]
    for op in op_list:
        print(op)

    continue_calculator = True

    while continue_calculator:

        ops = input("Pick an operation: ")

        n2 = int(input("Enter a second number: "))

        result = operation(n1,n2,ops)

        print(f"{n1} {ops} {n2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if cont == 'y':
            n1 = result
            operation(n1,n2,ops)

        elif cont == 'n':
            continue_calculator = False
            os.system('cls')
            calculator()

calculator()