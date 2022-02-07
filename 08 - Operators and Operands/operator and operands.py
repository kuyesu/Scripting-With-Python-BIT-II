"""
These are operators in python

-Comparison Operators
-Arithmetic Operators
-Membership Operators
-Assignment Operators
-Logical Operators

"""

"""
Arithmetic Operators
[
    +
    /
    -
    *
    %
]
"""

""" Examples """
num1 = 2
num2 = 3
sum = num1 + num2

print(sum)


""" 
    Comparison Operators
    
    <
    >
    =>
    =<
    !=
    ==
"""

""" Examples """

num1 = 2
num2 = 3
sum = num1 > num2

# print("num2 is greater than num2: ", sum)

if num1 > num2:
    print("num1 is less than num2")
elif num1 == num2:
    print("num2 is equal to num1 ")

elif num1 != num2:
    print("num1 is not equal num2")

else:
    print("num2 is greater than num1")



""" 
    Logical Operators 
    
    and 
    not
    or

"""

""" Examples """

num1 = 2
num2 = 3
num3 = 4

if num1 > num2 and num2 < num3:
    print("num1 is the smallest")

elif num1 > num2 or num2 < num3:
    print("num2 is greater than num1 but less than num3")

x = 4
y = 6
z = 8
if  x > y and z < y:
    print("yes")
elif x > z or y < x:
    print("maybe")
else:
    print("x is least of all")

print(x in range(3))
print(x in range(6))



""" 
    Assignment
    +=
    -=
    /=
    *=
"""

""" Example """
num1 = 2
num2 = 3

sum = num1 + num2

sum += 9
print(sum)

sum += num1
print(sum)

sum *= num1
print(sum)

sum -= num1
print(sum)

sum /= num1
print(sum)


a = 1
b = 9
c = 10
num = a+b+c
print(num)
num /= c
print(num)
num += a
num *= c
num /= c
print(num)


""" 
    Membership Operation
    is
    is not
    in

"""

""" Example """

name = "Bamukunda Joanitah"

print("Bam" in name)

if "Zam" in name:
    print("Bam is found in name")
else:
    print("The letters are not found in name")

action = "Joan is eating beef."
if "eat" in action:
    print("eating in progress")
else:
    print("nothing")