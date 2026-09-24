# Given:
# employee1_skills = {"Python", "SQL", "Django", "Git"}
# employee2_skills = {"Python", "React", "Git", "Docker"}
# Write a program to find:
# Skills known by both employees.
# Skills known only by Employee 1.
# Skills known only by Employee 2.
# All unique skills.
# Whether both employees have Python.
# Whether one employee's skills are a subset of the other's.


employee1_skills = {"Python", "SQL", "Django", "Git"}
employee2_skills = {"Python", "React", "Git", "Docker"}

both_skills = employee1_skills.intersection(employee2_skills)

only_employee1_skills = employee1_skills.difference(employee2_skills)

only_employee2_skills = employee2_skills.difference(employee1_skills)

all_unique_skills = employee1_skills.union(employee2_skills)

print("Skills known by both employees:", both_skills)
print("Skills known only by Employee 1:", only_employee1_skills)
print("Skills known only by Employee 2:", only_employee2_skills)
print("All unique skills:", all_unique_skills)

if "Python" in employee1_skills and "Python" in employee2_skills:
    print("Both employees have Python")
else:
    print("Both employees do not have Python")

if employee1_skills.issubset(employee2_skills): 
    print("Employee 1 skills are a subset of Employee 2 skills") 
elif employee2_skills.issubset(employee1_skills): 
    print("Employee 2 skills are a subset of Employee 1 skills") 
else: 
    print("Skills are not a subset of the other")