# We can create our own functions based on our requirements.

# def - keyword used to declare a function
# function_name - any name given to the function
# arguments - any value passed to function
# return (optional) - returns value from a function

def greet():
    print('Hello World!')


# call the function
greet()

print('Outside function')


# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)


# function call with two values
add_numbers(5, 4)  # Sum: 9


# function definition
def find_square(num):
    result = num * num
    return result


# function call
square = find_square(3)

print('Square:', square)  # Square: 9
