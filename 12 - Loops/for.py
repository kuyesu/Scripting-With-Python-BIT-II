"""
Introduction to the if Statement
We’ll start by looking at the most basic type of if statement. In its simplest form, it looks like this:
"""


""" Syntax of for loop """
# if <expr>:
#     <statement>


"""
for Loops and the range() Function
The while loop keeps looping while its condition is True (which is the reason for its name), but what if you want to execute a block of code only a certain number of times? You can do this with a for loop statement and the range() function.

In code, a for statement looks something like for i in range(5): and includes the following:

The for keyword
A variable name
The in keyword
A call to the range() method with up to three integers passed to it
A colon
Starting on the next line, an indented block of code (called the for clause)
Let’s create a new program called fiveTimes.py to help you see a for loop in action.
"""

"""
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
"""


for name in ['Christopher', 'Susan']:
	print(name)


# printing triangle
for x in range(1, 30, 2):
    s = '*' * x
    print(s.center(30))



# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


""" Variables created in a loop will be accessible outside that loop
In the example belo              w, the names i, j and k are declared within a loop (or a pair of nested loops). 
Despite this, all these names are accessible to the toplevel coding area."""
for i in (range(1)):
    for j in (range(10, 11)):
        print(i)
        print(j)
        k = i + j
        print(k)
        print()
 
 
print("Outside loop i:" + str(i))
print("Outside loop j:" + str(j))
print("Outside loop k:" + str(k))



# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)