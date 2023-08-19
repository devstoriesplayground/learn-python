# Python try-except is used to block that allows your program to alternate action incase there is an error occurs.
x = 9
try:
  if x == 9:
    print("Equals")
except TypeError:
  print("Invalid value")