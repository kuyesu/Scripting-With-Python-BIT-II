names = ['Christopher', 'Susan']
index = 0
while index < len(names):
	print(names[index])
	# Change the condition!!
	index = index + 1


# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


"""An example is shown below:"""

days = 0    
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
while days < 7:
   print("Today is " + week[days])
   days += 1


"""
Line-by-Line Explanation of the above CODE:

	- the variable ‘days’ is set to a value 0.
	- a variable week is assigned to a list containing all the days of the week.
	- while loop starts
	- the block of code will be executed until the condition returns ‘true’.
	- the condition is ‘days<7’ which rougly says run the while loop till the point the variable days is less than 7
	- So when the days=7 the while loop stops executing.
	- the days variable gets updated on every iteration.
	- When the while loop runs for the first time the line ‘Today is Monday’ is printed onto the console and the variable days becomes equal to 1.
	- Since the variable days is equal to 1 which is less than 7 so the while loop is executed again.
	- It goes on again and again and when the console prints ‘Today is Sunday’ the variable days is now equal to 7 and the while loop stops executing.
"""


"""
An Annoying while Loop
Here’s a small example program that will keep asking you to type, literally, your name. Select File ▸ New to open a new file editor window, enter the following code, and save the file as yourName.py:
"""



"""
➊ name = ''
➋ while name != 'your name':
       print('Please type your name.')
    ➌ name = input()
➍ print('Thank you!')
"""


"""break Statements
There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.

Pretty simple, right? Here’s a program that does the same thing as the previous program, but it uses a break statement to escape the loop. Enter the following code, and save the file as yourName2.py:
"""


"""
➊ while True:
       print('Please type your name.')
    ➋ name = input()
    ➌ if name == 'your name':
        ➍ break
➎ print('Thank you!')
"""



"""

continue Statements
Like break statements, continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. (This is also what happens when the execution reaches the end of the loop.)

Let’s use continue to write a program that asks for a name and password. Enter the following code into a new file editor window and save the program as swordfish.py.
"""

"""
 while True:
      print('Who are you?')
      name = input()
    ➊ if name != 'Joe':
        ➋ continue
       print('Hello, Joe. What is the password? (It is a fish.)')
    ➌ password = input()
       if password == 'swordfish':
        ➍ break
➎ print('Access granted.') 
"""