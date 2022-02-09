# """ CONTROL STATEMENT"""

# """ if functions"""

# """
# syntax

# if <condition>:
#     ...
#     statement
# """

# num1 = 2
# num2 = 3
# num3 = 4
# if num1 < num2 and num2 < num3:
#     print("Yes, num1 is less than num2")

# name = "My favorite color is blue"

# if "color" in name:
#     print("Color found in the statement")


# """
# syntax of if else

# if <condition>:
#     ...
#     stmt
# else:
#     ...
#     stmt
# """

# num1 = 2
# num2 = 3
# num3 = 4    
# if num1 < num2 and num2 > num3:
#     print("Yes, num1 is less than num2")
# else:
#     print("No, num2 is less than num3")


""" Quiz game """


"""question 1"""
question = "What is the highest mountain in Uganda?"
answer = "Rwenzori"

print("\n\n ##### Quize Game ####\n")
print(question)
print("1. Mount Elgon\n2. Mount Rwenzori\n3. Mount Moroto\n4. Mount Mufumbiro\n")

choice = input("Enter your answer: ")

if choice.lower() == answer.lower():
    print(f"\nYes, congragulation!\n Your answer {choice} is correct")

else:
    print(f"Oosh, sorry your answer {choice} was not correct\nTry again later")

"""question 2"""
question = "What is the second highest mountain in Uganda?"
answer = "Rwenzori"

print("\n")
print(question)
print("1. Mount Elgon\n2. Mount Rwenzori\n3. Mount Moroto\n4. Mount Mufumbiro\n")

choice = input("Enter your answer: ")

if choice.lower() == "Rwenzori".lower():
    print(f"\nYes, congragulation!\n Your answer {choice} is correct")

else:
    print(f"Oosh, sorry your answer {choice} was not correct\nTry again later")