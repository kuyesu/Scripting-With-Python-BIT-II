print("Hello World")
print("BIT is fun")
print('Hello WOLRD')

name = "Rogers"
print(name)

name = "Rogers"
age = 8
#print("My name is " + name + "and i am " + age " year old" )

print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

print(name.upper())

print(name.capitalize())

print(name.replace("Rogers", "Joan"))


print(f"{name} \n" * 8)


"""Python DATATYPES

Numeric datatypes
    - integers
    - float
    - complex numbers

Strings
Sequence dataypes
    - Lists (arrays)
    - Sets
    - tuple

Dictionary

"""

"""Integer"""

age = 56
print(type(age))


num1 = 23
num2 = 40

sum = num1 + num2
diff = num1 - num2
div = num1 / num2
mult = num1 * num2
raise_to_power = num1**num2


print(sum)
print(diff)
print(div)
print(mult)
print(raise_to_power)

print(f"{num1} and another numer is {num2}")
print(num1+num2)


"""floats"""

average_height = 45.901
another_hieght = 6.903

sum = average_height + another_hieght
print(sum)
print(type(sum))


"""Complex Numbers"""

number = 5 + 6j
print(type(number))


"""Lists"""


names = ["Rogers", "Joan", "Justus", "Arnold", "Bridget"]
print(type(names))

names.append("Doreen")

names.insert(2, "Tonny")
names.insert(4, "Isaac")

# names.remove("Isaac")
# names.pop()
# names.pop()


print(names)

print(names[3])

print(names[:])

print(names[0:2])

print(names[3:5])

print(names[3:])

print(names[::-1])