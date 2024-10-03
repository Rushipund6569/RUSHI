def add_ten_numbers():
    """Adds 10 numbers provided by the user."""

    sum = 0
    for i in range(10):
        number = float(input(f"Enter number {i + 1}: "))
        sum += number
    return sum

# Get the sum from the function
result = add_ten_numbers()

# Print the result
print("The sum of the 10 numbers is:", result)
