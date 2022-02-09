


print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


# lst = [ ]
# n = int(input("Enter number of elements : "))
 
# for i in range(0, n):
#     ele = [input(), int(input())]
#     lst.append(ele)
     
# print(lst)


"""
marks = {}
counter = int(input("Enter the number of time: "))

for i in range(0, counter):
    student_name = input("Enter student's name: ")
    student_mark = input("Enter student's mark: ")

marks = {student_name.title():student_mark}
"""

# print(marks)


marks = {}

for i in range(3):
    student_name = input("Enter student's name: ")
    student_mark = input("Enter student's mark: ")
    stduent_age = input("Enter the age if the stiudebt yiuyw ahbwjt ti ahee: ")
    # marks[student_name.title()] = student_mark
    # marks[student_mark.title()] = student_name
    marks[student_name.title()] = f"Mark:- {student_mark} Age:- {str(stduent_age)}"




print(marks)