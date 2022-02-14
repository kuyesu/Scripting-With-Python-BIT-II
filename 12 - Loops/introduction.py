""" Lopps Types and description """


"""
1. For loops
2. While loops
3. Break and continue
4. Pass
"""

"""
While loops

while loop Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

    - Syntax of a while loop
    - While loop is used to execute a block of code as long as the condition is true.
    
    while condition:
        statements

    while True: # Infinite loop
        statements

    while False: # Empty loop
        statements

    while None: # Empty loop
        statements

    while 0: # Empty loop
        statements

    while 1: # Infinite loop
        statements

    while -1: # Infinite loop
        statements

    while 0.0: # Empty loop
        statements

    while 0.1: # Infinite loop
        statements

    while 0.0e0: # Empty loop
        statements

    while 0.1e0: # Infinite loop
        statements

"""

"""Example 1: While loop"""


# While loop
i = 1
while i < 10:
    print(i)
    i += 1


"""Example 2: Infinite loop"""  

# Infinite loop
while True:
    print("Hello")


"""Example 3: Empty loop"""


# Empty loop
while False:
    print("Hello")


"""Example 4: Empty loop"""


# Empty loop
while None:
    print("Hello")



"""Quiz 1: What is the output of the following code?"""


# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8


"""Quiz 2: What is the output of the following code?"""


"""quiz game using while loop"""


question = "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow"
answer = "b"


while True:
    print(question)
    guess = input()
    if guess == answer:
        print("Correct!")
        break
    else:
        print("Incorrect!")



questions = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are Bananas?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are Strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are pears?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are grapes?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are lemons?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are limes?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are oranges?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are bananas?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are pears?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are grapes?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are lemons?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are limes?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are oranges?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow",
    "What color are bananas?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow"
]


answers = [
    "b",
    "d",
    "a",
    "b",
    "d",
    "a",
    "b",
    "d",
    "a",
    "b",
    "d",
    "a",
    "b",
    "d",
    "a",
    "b",
    "d",
    "a",
]


score = 0
for i in range(len(questions)):
    print(questions[i])
    guess = input()
    if guess == answers[i]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
print("You got", score, "out of", len(questions), "correct.")

