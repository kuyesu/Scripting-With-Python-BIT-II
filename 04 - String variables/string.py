""" String dataType"""

name = "Joan"
likes = "Chips"
year = "year two"
age = 15

"Joan is 15 and she is in year two. She likes chips"

""" String concatination"""
""" There are three ways of concatinating strings"""

""" 
- +
- f function
- format function
"""

name = "Joan"
likes = "Chips"
year = "year two"
age = 15

#"Joan is 15 and she is in year two. She likes chips"
print(name + " " + "is " + str(age) + " she is in " + year + "She likes " + likes)


"Joan is 15 and she is in year two. She likes chips"
# print("{} is {} and she is in {}. She likes {}".format(name, age, likes))

""" getting input from the user"""

name = input("Enetr your name: ")
age = str(input("Enter your age: "))
likes = input("Enter what you like: ")

print(f"{name} is {age} and she likes {likes}")

