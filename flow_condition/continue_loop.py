# We can use the continue statement with the for loop to skip the current iteration of the loop.
# Then the control of the program jumps to the next iteration.

for i in range(5):
    if i == 3:
        continue
    print(i)
    