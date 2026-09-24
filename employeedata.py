# For the following employee data
# {
#     "id": 101,
#     "name": "Anu",
#     "designation": "Python Developer",
#     "skills": ["Python", "Django", "SQL"],
#     "experience": 4,
#     "salary": 65000
# }
# Create separate functions for each operation:
# add_employee()
# display_employees()
# search_employee()
# update_employee()
# delete_employee()
# calculate_average_salary()
# find_employees_by_skill()
# find_experienced_employees()
# The program should handle invalid user input gracefully.
# Use exception handling to resolve situations such as:
# Employee ID entered as text instead of a number.
# Negative salary.
# Negative experience.
# Empty employee name.
# Duplicate employee ID.
# Searching for a non-existing employee.
# Invalid menu option.
# Invalid data type.

employees = [
    {
        "id": 101,
        "name": "Anu",
        "designation": "Python Developer",
        "skills": ["Python", "Django", "SQL"],
        "experience": 4,
        "salary": 65000
    }
]

def add_employee():
    try:
        emp_id = int(input("Enter employee ID: "))
        for emp in employees:
            if emp["id"] == emp_id:
                print("Employee ID already exists.")
                return
        name = input("Enter employee name: ").strip()
        if not name:
            print("Employee name cannot be empty.")
            return
        designation = input("Enter designation: ")
        skills_input = input("Enter skills (comma-separated): ").strip()

        if not skills_input:
            print("Skills cannot be empty.")
            return

        skills = [skill.strip() for skill in skills_input.split(",")]
        
        experience = int(input("Enter years of experience: "))
        if experience < 0:
            print("Experience cannot be negative.")
            return
        salary = float(input("Enter salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
        
        new_employee = {
            "id": emp_id,
            "name": name,
            "designation": designation,
            "skills": [skill.strip() for skill in skills],
            "experience": experience,
            "salary": salary
        }
        employees.append(new_employee)
        print("Employee added successfully.")
    except ValueError:
        print("Invalid input. Please enter the correct data type.")


def display_employees():
    if not employees:
        print("No employees to display.")
        return
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Designation: {emp['designation']}, "
              f"Skills: {', '.join(emp['skills'])}, Experience: {emp['experience']} years, "
              f"Salary: ${emp['salary']:.2f}")

def search_employee():
    try:
        emp_id = int(input("Enter employee ID to search: "))
        for emp in employees:
            if emp["id"] == emp_id:
                print(f"ID: {emp['id']}, Name: {emp['name']}, Designation: {emp['designation']}, "
                      f"Skills: {', '.join(emp['skills'])}, Experience: {emp['experience']} years, "
                      f"Salary: ${emp['salary']:.2f}")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a valid employee ID.")


def update_employee():
    try:
        emp_id = int(input("Enter employee ID to update: "))
        for emp in employees:
            if emp["id"] == emp_id:
                name = input(f"Enter new name (current: {emp['name']}): ")
                if name:
                    emp["name"] = name
                designation = input(f"Enter new designation (current: {emp['designation']}): ")
                if designation:
                    emp["designation"] = designation
                skills = input(f"Enter new skills (comma-separated, current: {', '.join(emp['skills'])}): ")
                if skills:
                    emp["skills"] = [skill.strip() for skill in skills.split(",")]
                experience = input(f"Enter new years of experience (current: {emp['experience']}): ")
                if experience:
                    experience = int(experience)
                    if experience < 0:
                        print("Experience cannot be negative.")
                        return
                    emp["experience"] = experience
                salary = input(f"Enter new salary (current: ${emp['salary']:.2f}): ")
                if salary:
                    salary = float(salary)
                    if salary < 0:
                        print("Salary cannot be negative.")
                        return
                    emp["salary"] = salary
                print("Employee updated successfully.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter the correct data type.")

def delete_employee():
    try:
        emp_id = int(input("Enter employee ID to delete: "))
        for emp in employees:
            if emp["id"] == emp_id:
                employees.remove(emp)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a valid employee ID.")


def calculate_average_salary():
    if not employees:
        print("No employees to calculate average salary.")
        return
    total_salary = sum(emp["salary"] for emp in employees)
    average_salary = total_salary / len(employees)
    print(f"Average Salary: ${average_salary:.2f}")


def find_employees_by_skill():
    skill = input("Enter skill to search for: ").strip()
    found = False
    for emp in employees:
        if skill in emp["skills"]:
            print(f"ID: {emp['id']}, Name: {emp['name']}, Designation: {emp['designation']}, "
                  f"Skills: {', '.join(emp['skills'])}, Experience: {emp['experience']} years, "
                  f"Salary: ${emp['salary']:.2f}")
            found = True
    if not found:
        print("No employees found with the specified skill.")


def find_experienced_employees():
    try:
        min_experience = int(input("Enter minimum years of experience: "))
        if min_experience < 0:
            print("Experience cannot be negative.")
            return
        found = False
        for emp in employees:
            if emp["experience"] >= min_experience:
                print(f"ID: {emp['id']}, Name: {emp['name']}, Designation: {emp['designation']}, "
                      f"Skills: {', '.join(emp['skills'])}, Experience: {emp['experience']} years, "
                      f"Salary: ${emp['salary']:.2f}")
                found = True
        if not found:
            print("No employees found with the specified experience level.")
    except ValueError:
        print("Invalid input. Please enter a valid number for experience.")


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Calculate Average Salary")
        print("7. Find Employees by Skill")
        print("8. Find Experienced Employees")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            calculate_average_salary()
        elif choice == '7':
            find_employees_by_skill()
        elif choice == '8':
            find_experienced_employees()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


main()