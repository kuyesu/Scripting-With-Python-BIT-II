"""
Introduction to the if Statement
We’ll start by looking at the most basic type of if statement. In its simplest form, it looks like this:
"""


""" Syntax of for loop """
# if <expr>:
#     <statement>





for name in ['Christopher', 'Susan']:
	print(name)


# printing triangle
for x in range(1, 30, 2):
    s = '*' * x
    print(s.center(30))




# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)