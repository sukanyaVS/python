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