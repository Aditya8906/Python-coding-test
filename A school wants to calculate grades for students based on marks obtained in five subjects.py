#  A school wants to calculate grades for students based on marks obtained in five subjects. 
def calculate_grade(marks):
    average_mark = sum(marks) / len(marks)
    
    if average_mark >= 90:
        grade = 'A'
    elif average_mark >= 80:
        grade = 'B'
    else:
        grade = 'C'
    
    return average_mark, grade
# Taking input for marks of five subjects
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
average_mark, grade = calculate_grade(marks)
print(f"Average Mark: {average_mark:}")
print(f"Grade: {grade}")

# Output:

"""Enter marks for subject 1: 90
Enter marks for subject 2: 85
Enter marks for subject 3: 90
Enter marks for subject 4: 95
Enter marks for subject 5: 60
Average Mark: 84.00
Grade: B"""

"""Enter marks for subject 1: 90
Enter marks for subject 2: 95
Enter marks for subject 3: 99
Enter marks for subject 4: 98
Enter marks for subject 5: 94
Average Mark: 95.2
Grade: A"""