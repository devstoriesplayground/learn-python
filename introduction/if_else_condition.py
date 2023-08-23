# It supports logical conditions. You can add multiple conditions to catch different scenarios

age = input("Enter your age:")
if int(age) <= 18:
    print("You're not allowed to vote")
elif int(age) >= 18:
    print("You're allowed to vote")
else:
    print('Invalid. Please try again.')