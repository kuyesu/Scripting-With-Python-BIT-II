"""While loop"""

attempt = 3
while attempt <= 3:
    print("What is your name?")
    answer = "Bridget"
    name = input("Enter name: ")
    if name == answer:
        print("CORRECT !")
        break
    else:
        print("Wrong")
        print(f"You are left {attempt-1}/3")

    attempt -= 1
    if attempt == 0:
        break
    pass


student = {"name" : "Bridget", "age" : 24}

print(f" name is : { (student['name'])} and age is: { (student['age'])}")