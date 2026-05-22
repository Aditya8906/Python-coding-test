"""A company wants to identify whether an employee is eligible for a bonus based on attendance percentage and
 performance rating."""

def check_bonus_eligibility(attendance_percentage, performance_rating):
        if (attendance_percentage >= 90 and performance_rating >= 4) or (attendance_percentage >= 80 and performance_rating >= 4.5):
            return "Eligible for bonus"
        else:
            return "Not eligible for bonus"

attendance = float(input("Enter attendance percentage: "))
performance = float(input("Enter performance rating: "))
print(check_bonus_eligibility(attendance, performance))

# Output:
"""Enter attendance percentage: 89
Enter performance rating: 2
Not eligible for bonus"""

"""Enter attendance percentage: 93
Enter performance rating: 4.7
Eligible for bonus"""

"""Enter attendance percentage: 20
Enter performance rating: 5
Not eligible for bonus"""
