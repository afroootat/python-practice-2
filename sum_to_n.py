# Ask the user to enter a number
user_number = int(input("Enter a number: "))

# Start with 0, this will hold the total sum
sum_of_numbers = 0

# Loop from 1 to the number the user gave (inclusive)
for i in range(1, user_number + 1):
    sum_of_numbers += i  # Add each number to the total

# Print the final result
print(f"The total sum of numbers from 1 to {user_number} is {sum_of_numbers}")