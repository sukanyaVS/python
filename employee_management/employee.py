from exceptions import (
    DuplicateEmployeeError,
    EmployeeNotFoundError
)

from validation import (
    validate_name,
    validate_salary,
    validate_experience
)


# Employee data
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


# Add employee
def add_employee():
    employee_id = int(input("Enter employee ID: "))

    # Check duplicate employee ID
    for employee in employees:
        if employee["id"] == employee_id:
            raise DuplicateEmployeeError(
                "Employee ID already exists."
            )

    name = validate_name(
        input("Enter employee name: ")
    )

    designation = input(
        "Enter designation: "
    ).strip()

    if not designation:
        raise ValueError(
            "Designation cannot be empty."
        )

    skills_input = input(
        "Enter skills separated by comma: "
    ).strip()

    if not skills_input:
        raise ValueError(
            "Skills cannot be empty."
        )

    skills = [
        skill.strip()
        for skill in skills_input.split(",")
    ]

    experience = int(
        input("Enter years of experience: ")
    )

    validate_experience(experience)

    salary = float(
        input("Enter salary: ")
    )

    validate_salary(salary)

    new_employee = {
        "id": employee_id,
        "name": name,
        "designation": designation,
        "skills": skills,
        "experience": experience,
        "salary": salary
    }

    employees.append(new_employee)

    print("Employee added successfully.")


# Display all employees
def display_employees():
    if not employees:
        print("No employees found.")
        return

    print("\n===== Employee List =====")

    for employee in employees:
        print("-------------------------")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Designation:", employee["designation"])
        print("Skills:", ", ".join(employee["skills"]))
        print("Experience:", employee["experience"], "years")
        print("Salary:", employee["salary"])


# Search employee
def search_employee():
    employee_id = int(
        input("Enter employee ID to search: ")
    )

    for employee in employees:
        if employee["id"] == employee_id:
            print("\n===== Employee Found =====")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Designation:", employee["designation"])
            print("Skills:", ", ".join(employee["skills"]))
            print("Experience:", employee["experience"], "years")
            print("Salary:", employee["salary"])
            return

    raise EmployeeNotFoundError(
        "Employee not found."
    )


# Update employee
def update_employee():
    employee_id = int(
        input("Enter employee ID to update: ")
    )

    for employee in employees:
        if employee["id"] == employee_id:

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Designation")
            print("3. Skills")
            print("4. Experience")
            print("5. Salary")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = validate_name(
                    input("Enter new name: ")
                )

                employee["name"] = name

            elif choice == "2":
                designation = input(
                    "Enter new designation: "
                ).strip()

                if not designation:
                    raise ValueError(
                        "Designation cannot be empty."
                    )

                employee["designation"] = designation

            elif choice == "3":
                skills_input = input(
                    "Enter new skills separated by comma: "
                ).strip()

                if not skills_input:
                    raise ValueError(
                        "Skills cannot be empty."
                    )

                employee["skills"] = [
                    skill.strip()
                    for skill in skills_input.split(",")
                ]

            elif choice == "4":
                experience = int(
                    input("Enter new experience: ")
                )

                validate_experience(experience)

                employee["experience"] = experience

            elif choice == "5":
                salary = float(
                    input("Enter new salary: ")
                )

                validate_salary(salary)

                employee["salary"] = salary

            else:
                raise ValueError(
                    "Invalid update option."
                )

            print("Employee updated successfully.")
            return

    raise EmployeeNotFoundError(
        "Employee not found."
    )


# Delete employee
def delete_employee():
    employee_id = int(
        input("Enter employee ID to delete: ")
    )

    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)

            print("Employee deleted successfully.")
            return

    raise EmployeeNotFoundError(
        "Employee not found."
    )


# Calculate average salary
def calculate_average_salary():
    if not employees:
        print("No employees available.")
        return

    total_salary = 0

    for employee in employees:
        total_salary += employee["salary"]

    average_salary = total_salary / len(employees)

    print(
        "Average Salary:",
        round(average_salary, 2)
    )


# Find employees by skill
def find_employees_by_skill():
    skill = input(
        "Enter skill to search: "
    ).strip()

    if not skill:
        raise ValueError(
            "Skill cannot be empty."
        )

    found = False

    print(
        "\n===== Employees with",
        skill,
        "====="
    )

    for employee in employees:

        for employee_skill in employee["skills"]:

            if employee_skill.lower() == skill.lower():

                print(
                    "ID:",
                    employee["id"],
                    "| Name:",
                    employee["name"]
                )

                found = True
                break

    if not found:
        print(
            "No employees found with this skill."
        )


# Find experienced employees
def find_experienced_employees():
    minimum_experience = int(
        input(
            "Enter minimum experience: "
        )
    )

    validate_experience(
        minimum_experience
    )

    found = False

    print(
        "\n===== Experienced Employees ====="
    )

    for employee in employees:

        if employee["experience"] >= minimum_experience:

            print(
                "ID:",
                employee["id"],
                "| Name:",
                employee["name"],
                "| Experience:",
                employee["experience"],
                "years"
            )

            found = True

    if not found:
        print(
            "No employees found."
        )