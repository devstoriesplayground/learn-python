def add_number(num1, num2):
    total = num1 + num2
    return total


# input function allows user to input data

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

print("Total: ", add_number(first, second))
