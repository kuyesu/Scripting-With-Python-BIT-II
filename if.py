"""If function called conditionl statement. They are mainly used for validation"""

"""Syntax

if <condition>:
	statement

"""

num1 = 4
num2 = 5
num3 = 6

if num1 > num2:
	print("Number 1 is less than number 2")

else: 
	print("This false part")


if num2 < num1 and num2 < num3:
	print("Something here")

else:
	print("Nothing going on")


print(num1 > num2)
print(num2 < num1 and num2 < num3)

if num1 > num2:
	print("The first part is correct")

elif num1 == num2:
	print("The second is the correct")

else:
	print("nothing was correct above")



if num1 < num2:
	if num2 > num3:
		if num3 > num1:
			print("Wow, we nested and the codintions were true")

	else:
		print("Oosh, not quite")

else:
	print("That was false")



question = "1. What is the highest mountain in Uganda\na. Mount Elgon\nb. Mount Moroto\nc. Mount Rwenzori\nd. Mount Mufumbiro\n"
answer = "Rwenzori"


print("\n\n####Welcome to Quiz Game####\n")

print(question)

guess = input("Enter your answer: ")

if guess.lower() == answer.lower():
	print(f"wow, you got {guess} correct")
else:
	print(f"Oosh, sorry your answer {guess} is not correct, but the answer is {answer}")