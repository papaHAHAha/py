from random import randint
marks = []
length = int(input("write length of marks: "))
for i in range(length):
    marks.append(randint(1,5))
print(marks)
maxMark = max(marks)
minMark = min(marks)
for j in range(len(marks)):
    if marks[j] == maxMark:
        marks[j] = minMark
print(marks)
