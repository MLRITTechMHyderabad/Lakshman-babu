def Average_Grade(students):
    name_to_find = "Bruce"
    for name, grades in students.items():
        if name == name_to_find:
            print(f"Average Grade for {name}: {sum(grades) / len(name)}")
        
def Heihest_Grade(students):
    high_Avg = 0
    TopOne = ""

    for name, grades in students.items():
        Average = sum(grades) // len(grades)
        if Average > high_Avg:
            high_Avg = Average
            TopOne = name
    print(f"{TopOne} with the Highest average grade is: {high_Avg}")

def passedStudents(students):
    passCount = [(name, sum(grades)/len(grades)) for name, grades in students.items() if (sum(grades)/len(grades)) >= 50]
    print("Number of students who passed: " +str(len(passCount)))

#Dictionay
students = {
    "Tony":[90, 80, 70, 92, 68],
    "Steves":[78, 80, 65, 56, 89],
    "Bruce": [85, 76, 62, 43, 64],
    "Natasha": [25, 75, 64, 91, 71],
    "Thor": [85, 62, 71, 90, 63]
}

print(dict(students))
#Calling functions
Average_Grade(students)
Heihest_Grade(students)
passedStudents(students)