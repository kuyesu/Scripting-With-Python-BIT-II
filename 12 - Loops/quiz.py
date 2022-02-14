question = "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Yellow"
answer = "b"

attempt = 3
while attempt <= 3:
    print(question)
    guess = input()
    if guess == answer:
        print("Correct!")
        break
    else:
        print("Incorrect!")
        print(f"You have only {attempt-1}/3")

        attempt -= 1

        if attempt == 0:
            break



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

