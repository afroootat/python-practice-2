# List of numbers from 1 to 20
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Create an empty list to store even numbers
empty_list = []

# Loop through numbers and append even ones to the empty list
for num in numbers:
    if num % 2 == 0:
        empty_list.append(num)

# Print the list of even numbers
print(f"Even numbers: {empty_list}")