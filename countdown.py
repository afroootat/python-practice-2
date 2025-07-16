# Ask the user for a number to start the countdown from
number_from_user = int(input("Enter a starting number: "))

# Keep printing the number and reduce it by 1 each time
while number_from_user >= 0:
    print(number_from_user)
    number_from_user -= 1  # Subtract 1 each time until we reach 0