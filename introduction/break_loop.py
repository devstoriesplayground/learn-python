# Break loop is used to control sequence of the loop.
# It supposed to terminate the loop and move to the next line of code

x = 1

while x < 10:
    print(x)
    if x == 5:
        break
    x = x + 1
