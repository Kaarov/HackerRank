from collections import namedtuple

n = int(input())
ans = 0
students = []
Student = namedtuple('Student', input())

for i in range(n):
    student = tuple(input().split())
    students.append(Student(*student))

for i in students:
    ans += int(i.MARKS)

print(ans / len(students))

# Done ✅
