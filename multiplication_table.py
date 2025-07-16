# Ask the user to enter the number they want a multiplication table for
user_number = int(input("Enter a number: "))

# Loop from 1 to 12 to print the multiplication table
for i in range(1, 13):
    # Print each line of the table (e.g., 5 * 1 = 5)
    print(f"{user_number} * {i} = {user_number * i}")