# Ask the user to enter a number
user_number = int(input("Enter any number: "))

# Define a function to check if the number is even or odd
def number_checker(user_number):
    if user_number % 2 == 0:
        print(f"{user_number} is an even number.")
    else:
        print(f"{user_number} is an odd number.")

# Call the function with the user's number
number_checker(user_number)