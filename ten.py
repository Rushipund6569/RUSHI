def add_ten_numbers():
 

    sum = 0
    for i in range(5):
        number = float(input(f"Enter number {i + 1}: "))
        sum += number
    return sum


result = add_ten_numbers()


print("The sum of the 10 numbers is:", result)
