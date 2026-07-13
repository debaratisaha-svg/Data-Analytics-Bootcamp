marks=[85, 92, 78, 96, 88]
print ("Marks:", marks)
subjects=["python", "java", "c++", "html", "css"]
print("Subjects:", subjects)    
Students=["Debarati",21,"BCA", True]
print("Students:", Students)

cities=["Kolkata", "Mumbai", "Chennai", "Bangalore"]
print("Cities:", cities)

prices=[65000, 45000, 30000, 75000]
print("Prices:", prices)

#indexing
subjects=["python", "java", "c++", "html", "css"]
print("First subject:", subjects[0])
print("Second subject:", subjects[1])    

fruits = ["apple", "banana", "orange", "grapes"]
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
print("Last fruit:", fruits[-1])


marks=[85, 92, 78, 96, 88]
print("First mark:", marks[0])
print("Third mark:", marks[2])
print("Fifth mark:", marks[4])

#negetive indexing
Subjects=["python", "java", "c++", "html", "css"]
print("Last subject:", subjects[-1])
print("secondlast subject:",subjects[-2])

#updating list
marks = [85, 92, 78, 96, 88]
marks[3]=95
print (marks)
fruits = ["Apple","Mango","orange"]
fruits[-1]="Banana"
print(fruits)

#list Functions
marks = [85, 92, 78, 96, 88]
print("Length of marks list:", len(marks))

print("sum:",sum(marks))
print("average:", sum(marks)/len(marks))
print("maximum:", max(marks))
print("minimum:", min(marks))

marks.append(90)
print("Marks after appending:", marks)
marks.remove(78)
print("Marks after removing 78:", marks)
