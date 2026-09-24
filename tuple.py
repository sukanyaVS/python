# .Represent an employee using a tuple:
# employee = (
#     101,
#     "Anu",
#     "Python Developer",
#     4,
#     65000
# )
# Write a program to:
# Display each value separately.
# Access the employee's name and salary using indexing.
# Unpack the tuple into individual variables.
# Calculate a 10% salary increment.
# Create a new tuple containing the updated salary.


employee = ( 101, "Anu", "Python Developer", 4, 65000 )

print("Employee ID:", employee[0]) 
print("Employee Name:", employee[1]) 
print("Role:", employee[2]) 
print("Experience:", employee[3]) 
print("Salary:", employee[4])

# Accessing name and salary using indexing
name = employee[1]
salary = employee[4]
print("Employee Name:", name)
print("Salary:", salary)

# Unpacking the tuple into individual variables
id, name, role, experience, salary = employee

# Calculating a 10% salary increment
salary_increment = salary * 0.10
new_salary = salary + salary_increment

# Creating a new tuple with the updated salary
updated_employee = (id, name, role, experience, new_salary)

print("Updated Employee Tuple:", updated_employee)