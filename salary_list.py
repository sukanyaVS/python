# Given the following salaries:
# salaries = [35000, 42000, 55000, 67000, 48000, 72000, 39000]
# Write a program using only for loop and not any builtin functions  to:
# Display all salaries.
# Calculate the total salary.
# Calculate the average salary.
# Find the highest salary.
# Find the lowest salary.
# Count how many employees earn more than ₹50,000.
# Display all salaries above ₹50,000.

salaries = [35000, 42000, 55000, 67000, 48000, 72000, 39000]
total = 0
highest_salary = salaries[0]
lowest_salary = salaries[0]
count_above_50k = 0

print("All salaries")
print("=======================")
for salary in salaries:
    print(salary)

    if salary > highest_salary:
        highest_salary = salary
    if salary < lowest_salary:
        lowest_salary = salary
    if salary > 50000:
        count_above_50k += 1
        
    total += salary


average = total / len(salaries)
print("\nTotal salary: ", total)
print("Average salary: ", round(average, 2))
print("Highest salary: ", highest_salary)
print("Lowest salary: ", lowest_salary)
print("Number of employees earning more than 50,000:", count_above_50k)
print("\nSalaries above 50,000")
for salary in salaries:
    if salary > 50000:
        print(salary)