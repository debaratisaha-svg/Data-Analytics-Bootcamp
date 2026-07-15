marks= [85,92,78,96,88 ]
total =0
for mark in marks:
    total += mark
print("Marks:", marks)
print("Total marks:", total)
print("Average marks:", total / len(marks))

#find the highest and lowest marks
highest = marks[0]
for mark in marks:
    if mark >highest:
        highest = mark
print("Highest marks:", highest)
lowest = marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark
print("Lowest marks:", lowest)

pass_count = 0
for mark in marks:
    if mark >= 80:
        pass_count += 1
print("Number of students who passed:", pass_count)

above_90 = 0
for mark in marks:
    if mark > 90:
        above_90 += 1   
print("Number of students who scored above 90:", above_90)