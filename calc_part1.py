from art import logo

#add function
def add(n1, n2):
    return n1 + n2

# Subtract function
def subtract(n1, n2):
    return n1 - n2

# multiply function
def multiply(n1, n2):
    return n1 * n2

#division function
def division(n1, n2):
    return n1 / n2

# dictionary will allow us to call each function to perform calculations
operations = { "+": add,
              "-": subtract,
              "*": multiply,
              "/": division
}


def calculator():
    print(logo)

    # asks user for their first input.
    num1 = float(input("What is your first number? "))

    # provide user with list of operators to help them select the operation
    for operator in operations:
        print(operator)

    # function that takes in the users  number input and calculation selection
    def answer():
        calc = operations[operation_selection]
        answer_one = calc(num1, num2)
        return answer_one

    # control variable for while loop.
    if_continue_calculating = True

    while if_continue_calculating:

        operation_selection = input("Pick an operation symbol: ")
        num2 = float(input("What is your next number? "))
        print(f"{num1} {operation_selection} {num2} = {answer()}")

        continue_calculations = input(f"Type y to continue calculating with {answer()} or type n to start a new calculation. ").lower()
        if continue_calculations == "y":
            num1 = answer()
            print(f"{num1} {operation_selection} {num2} = {answer()}")
            num1 = answer()
        elif continue_calculations == "n":
            if_continue_calculating = False
            # recursion
            calculator()
        else:
            print("Incorrect entry. Please type y to continue or n to exit ")

calculator()

