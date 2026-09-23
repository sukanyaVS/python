# Write a program that accepts:
# Employee name
# Number of tasks completed
# Number of tasks assigned
# Average customer rating
# Calculate the task completion percentage.
# Determine the performance level:
# .Completion >= 90% AND rating >= 4.5 → Excellent
# Completion >= 75% AND rating >= 4.0 → Good
# Completion >= 60% AND rating >= 3.0 → Average
# Otherwise → Needs Improvement

employee_name = input("Enter employee name: ")
tasks_assigned = int(input("Enter number of tasks assigned: "))
tasks_completed = int(input("Enter number of tasks completed: "))
customer_rating = float(input("Enter average customer rating: "))

completion_percentage = (tasks_completed / tasks_assigned) * 100

if (completion_percentage >= 90 and customer_rating >= 4.5):
    performance_level = "Excellent"
elif (completion_percentage >= 75 and customer_rating >= 4.0):
    performance_level = "Good"
elif (completion_percentage >= 60 and customer_rating >= 3.0):
    performance_level = "Average"
else:
    performance_level = "Needs Improvement"

print("Employee Name:", employee_name)
print("Task Completion Percentage:", completion_percentage)
print("Customer Rating:", customer_rating)
print("Performance Level:", performance_level)
