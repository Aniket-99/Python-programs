from collections import namedtuple

total_cases = int(input())

fields = input().split()

total = 0

for i in range(total_cases):
    students = namedtuple('students',fields)
    ID, MARKS, NAME, CLASS = input().split()
    student = students(ID, MARKS, NAME, CLASS)
    total += int(student.MARKS)
    average = total/total_cases
print(average)
