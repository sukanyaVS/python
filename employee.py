
# Create a Python program to store the following information about an employee:
    # Employee name
    # Employee ID
    # Years of experience
    # Current salary
    # Programming languages known
    # Whether the employee is currently assigned to a project
# The program should:
    #1 Store each value using an appropriate Python data type.
    #2 Display the employee information in a readable format.
    #3 Calculate the employee's salary after a 10% increment.
    #4 Display the number of programming languages known.
    #5 Display whether the employee is eligible for project allocation based on:
            # Experience ≥ 2 years
            # Currently not assigned to a project


#1.

employee_id = 220
employee_name = "Greeshma Merin Lal"
years_of_experience = 3.5
current_salary = 40000.0
programming_languages = ["Python", "React", "TypeScript"]
is_currently_assigned = False

#2.

print("Employee Information")
print("--------------------")
print("Name:", employee_name)
print("Employee ID:", employee_id)
print("Years of Experience:", years_of_experience)
print(f"Current Salary: ₹{current_salary:.2f}")
print("Programming Languages:", programming_languages)
print(f"Currently Assigned: {is_currently_assigned}")

#3.

increment = current_salary * 0.10
new_salary = current_salary + increment
print(f"Salary after 10% increment: ₹{new_salary:.2f}")

#4.

number_of_languages = len(programming_languages)
print("Number of Programming Languages:", number_of_languages)

#5.

if (years_of_experience >= 2) and (not is_currently_assigned):
    print("The employee is eligible for project allocation.")
else:
    print("The employee is not eligible for project allocation.")