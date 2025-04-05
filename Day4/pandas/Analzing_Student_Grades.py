import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)

#Find the average marks for each subject
avg_marks = df.groupby('Subject')['Marks'].mean()
print("Average Marks by Subjects:\n", avg_marks)

#Students who scored > 85 and had < 90% attendance
high_score_low_attendance = df[(df['Marks'] > 85) & (df['Attendance'] < 90)]
print("High scorers with low attendance:\n", high_score_low_attendance[['Student', 'Marks', 'Attendance']])


#Add a new column "Grade"
def assign_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Marks'].apply(assign_grade)
print("Data with Grades:\n", df[['Student', 'Marks', 'Grade']])

#Count how many students received each grade
grade_counts = df['Grade'].value_counts()
print("Grade Distribution:\n", grade_counts)

#Correlation between Marks and Attendance
correlation = df['Marks'].corr(df['Attendance'])
print(f"Correlation between Marks and Attendance: {correlation:.2f}")
