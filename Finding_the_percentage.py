# You have a record of N students.
# Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
# The marks can be floating values.
# The user enters some integer N followed by the names and marks for N students.
# You are required to save the record in a dictionary data type.
# The user then enters a student's name.
# Output the average percentage marks obtained by that student, correct to two decimal places.

n = int(input())
student_marks = {}

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
temp = student_marks.get(query_name)
a = (sum(temp)/len(temp))
print(format(a, '.2f'))