def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Get the first number
    num1 = float(input("Enter the first number: "))
    
    # Get the second number
    num2 = float(input("Enter the second number: "))
    
    # Get the operation
    print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
    operation = input("Enter the operation: ")
    
    # Perform the operation
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please try again.")
    
# Run the calculator
calculator()
