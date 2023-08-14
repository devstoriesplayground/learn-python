# assignment operators are used to assign values to a variable
x = 10
y = 20

z = 0
z += 3

a = 50
a &= 25

# arithmetic operators are used to perform mathematical operations
print(f'addition: {x + y}')
print(f'subtraction: {y - x}')
print(f'multiplication: {x * y}')
print(f'division: {y / x}')
print(f'modulus: {x % y}')
print(f'exponentiation: {x ** y}')
print(f'floor division: {x // y}')

# comparison operators are used to compare two variables
print(x==y)
print(y!=20)
print(a>=20)

# logical operators are used to combined conditional statements
if (x < 10 and y > 20): 
  print(True)
else: 
  print(False)


# identity operators are used to objects
fruits = ["apple", "banana", "grapes"]
juice = ["orange"]
print(fruits is juice)

# membership operators are used to test if a sequence is presented in a object
fruits = ["apple", "banana", "grapes"]
juice = ["orange"]
print(fruits not in juice)

# bitwise operators are used to compare binary numbers
print(8 >> 2)