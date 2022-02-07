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
