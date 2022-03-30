def fancy():
    print("hi, there")

fancy()

def name():
    print("my name is Doreen")

name()


def add():
    num1 = 3
    num2 = 5
    sum = num1+num2
    print(f"the sumof{num1}and{num2}is {sum}")
add()
def subtract():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    subtract = num1 - num2
    print(f"the differance of {num1}and{num2}is {subtract}")
subtract()


def division():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    division = num1 / num2
    print(f"the division of {num1}and{num2}is {division}")
division()
def multiplication():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    multiplication = num1 * num2
    print(f"the multiplication of {num1}and{num2}is {multiplication}")
multiplication()
def welcomesreen():
    username = input("enter your name")
    prin
    t(f"\n Hi {username}, welcome to my calculator")
    print("what do you want to perform\n 1. addition\n2.sutract\n3.division\n4.multiplication\n5.exit")
    choice = int(input("enter your choice"))
    welcomesreen()
if choice == 1:
   add()
elif choice == 2:
    subtract()
elif choice == 3:
    division()
elif choice == 4:
    multiplication()
elif choice == 5:
    exit
