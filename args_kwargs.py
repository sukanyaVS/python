# Create a function:
# def employee_report(name, *skills, **details):
#     pass
# The function should:
# Accept the employee's name.
# Accept any number of technical skills using *skills.
# Accept additional employee information using **details.
# Display all the information.

def employee_report(name, *skills, **details):
    print(f"Employee Name: {name}")
    
    if skills:
        print("Technical Skills:")
        for skill in skills:
            print(f"- {skill}")
    else:
        print("No technical skills provided.")
    
    if details:
        print("Additional Information:")
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        print("No additional information provided.")

employee_report("John Doe", "Python", "JavaScript", department="IT", position="Developer", experience=5)



# Create:
# def calculate_result(name, *marks, **student_info):
#     pass
# Example:
# calculate_result(
#     "Rahul",
#     85, 76, 92, 88, 79,
#     age=21,
#     course="Python",
#     batch="Morning"
# )
# Requirements:
# Calculate total and average.
# Determine grade.
# Display the student's additional information.
# Handle any number of subjects.

def calculate_result(name, *marks, **student_info):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Student Name: {name}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")
    
    if student_info:
        print("Additional Information:")
        for key, value in student_info.items():
            print(f"{key}: {value}")
    else:
        print("No additional information provided.")
