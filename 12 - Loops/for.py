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



""" Variables created in a loop will be accessible outside that loop
In the example below, the names i, j and k are declared within a loop (or a pair of nested loops). 
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