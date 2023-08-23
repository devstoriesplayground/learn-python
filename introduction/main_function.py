# Python programme uses the condition if __name__ == '__main__' to only run the code inside the if statement when the program is run directly by the Python interpreter. The code inside the if statement is not executed when the file's code is imported as a module


def step1():
   print("Executing the first step...")
def step2():
   print("Executing the second step...")
def step3():
   print("Executing the third step...")
def main():
   step1()
   step2()
   step3()
if __name__ == "__main__":
   main()