marks = [85, 92, 78, 96, 88]
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Number of Subjects:", len(marks))
print("performance:", end=" ")
if sum(marks) / len(marks) >= 90:
    print("Excellent")  
elif sum(marks) / len(marks) >= 80:
    print("Good")
elif sum(marks) / len(marks) >= 70:
    print("Average")
else:
    print("Needs Improvement")      
