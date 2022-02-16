"""Student data in a dictionary"""

student = {}

for i in range(3):
    name = input("Enter name: ")
    age = input("Enter age: ")
    reg = input("Enter registration number: ")
    student[name] = f"{age}, {reg}"
    dict(student)

print(student)