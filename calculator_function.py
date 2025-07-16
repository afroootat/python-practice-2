# Ask the user for two numbers
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

# Ask the user which operation they want to do
operation = input("Enter an operation(+, -, *, /): ")

# Define a function to do the math based on the operation
def calculate(num1, num2, operation):
    if operation == "+":
        print(f"Sum of {num1} and {num2} is {num1 + num2}")
    elif operation == "-":
        print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
    elif operation == "*":
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
    elif operation == "/":
        print(f"Division of {num1} and {num2} is {num1 / num2}")
    else:
        print("Enter a valid operation!")

# Call the function with the user's inputs
calculate(num1, num2, operation)