from Calc_art import logo


def add(n1, n2): 
    """Addition operation"""
    return n1 + n2

def subtract(n1, n2):
    """Subtraction operation"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplication operation"""
    return n1 * n2

def divide(n1, n2):
    """Division operation"""
    return n1 / n2

# Dictionary containing operation symbols and their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
    
def calculator():
    """Function to perform calculator operations"""
    print(logo)

# Getting the first number from the user
    num1 = float(input("What's the first number?: "))

    # Printing available operations
    for symbol in operations:
       print(symbol)
    should_continue = True

    while should_continue:
        # Getting operation symbol from the user
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        # Displaying the result of the calculation 
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # Displaying the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Asking if the user wants to continue with the reslut or start a new calculation
        if input(f"Type 'y'to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            # Restarting the calculator or ending the program
            should_continue = False
            calculator()

calculator()