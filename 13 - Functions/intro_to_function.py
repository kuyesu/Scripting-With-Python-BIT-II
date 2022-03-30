"""syntax
def function_name():
    ststement

def fancy():
    print("Hi, there!")
    #calling the function
fancy()

def add():
    number1= 45
    number2= 76
    sum = number1+number2
    fancy()
    print (f"The sum of {number1} and {number2} is {sum}")
add()
"""
def add():
    number1= int(input("Enter a number:"))
    number2= int(input("Enter a number:"))
    sum = number1+number2

    print (f"The sum of {number1} and {number2} is {sum}")
    welcomeScreen()

def difference():
    number1= int(input("Enter a number:"))
    number2= int(input("Enter a number:"))
    difference = number1-number2

    print (f"The difference of {number1} and {number2} is {difference}")
    welcomeScreen()

def divide():
    number1= int(input("Enter a number:"))
    number2= int(input("Enter a number:"))
    division = number1/number2

    print (f"The division of {number1} and {number2} is {division}")
    welcomeScreen()

def multiply():
    number1= int(input("Enter a number:"))
    number2= int(input("Enter a number:"))
    multiplication = number1*number2

    print (f"The multiplication of {number1} and {number2} is {multiplication}")
    welcomeScreen()
def terminate():
    print("Bye! Thanks for using our system")
    sys.Exit()

def welcomeScreen():
    username = input("Enter your Name:")
    print(f"Hi {username}!, Welcome to our calculator")
    print("What do you want to do\n1. Add numbers\n2. Subtract numbers\n3. Divide number\n4. Multiply number\n5. Exit(Pree any key)")
    choice = int(input("Enter your choice"))

    if choice ==1:
        add()
    elif choice==2:
        difference()
    elif choice==3:
        divide()
    elif choice==4:
        multiply()
    else:
        sys.exit()
welcomeScreen()
