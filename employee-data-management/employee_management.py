import json
from pathlib import Path


FILE_NAME = Path(__file__).with_name("employees.json")


def load_employees():
    try:
        with FILE_NAME.open("r") as file:
            employees = json.load(file)

        if not isinstance(employees, list):
            print("Invalid JSON data")
            return []
        return employees
    except FileNotFoundError:
        print(f"{FILE_NAME.name} file not found.")
        return []
    except json.JSONDecodeError:
        print(f"Invalid JSON data in {FILE_NAME.name}.")
        return []


def save_employees(employees):
    with FILE_NAME.open("w") as file:
        json.dump(employees, file, indent=4)
    print(f"Employee data saved to {FILE_NAME.name}.")


def find_employee_by_id(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None


def display_employees(employees):
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
        print("Salary:", f"{employee['salary']:.2f}")


def search_by_skill(employees):
    skill = input("Enter skill to search: ").strip()
    if not skill:
        print("Skill cannot be empty.")
        return

    matches = [
        employee
        for employee in employees
        if any(employee_skill.lower() == skill.lower() for employee_skill in employee["skills"])
    ]

    print("\n===== Search Results =====")
    if not matches:
        print("No employees found with this skill.")
        return

    for employee in matches:
        print(
            "ID:", employee["id"],
            "Name:", employee["name"],
            "Designation:", employee["designation"],
        )


def add_employee(employees):
    try:
        employee_id = int(input("Enter employee ID: "))
        if find_employee_by_id(employees, employee_id):
            print("An employee with this ID already exists.")
            return
        name = input("Enter employee name: ").strip()
        designation = input("Enter designation: ").strip()
        skills_text = input("Enter skills separated by commas: ").strip()
        salary = float(input("Enter salary: "))
    except ValueError:
        print("Invalid ID or salary.")
        return

    skills = [skill.strip() for skill in skills_text.split(",") if skill.strip()]
    if not name or not designation or not skills:
        print("Name, designation, and at least one skill are required.")
        return
    if salary < 0:
        print("Salary cannot be negative.")
        return

    employees.append({
        "id": employee_id,
        "name": name,
        "designation": designation,
        "skills": skills,
        "salary": salary,
    })
    save_employees(employees)
    print("Employee added successfully.")


def update_salary(employees):
    try:
        employee_id = int(input("Enter employee ID: "))
        new_salary = float(input("Enter new salary: "))
    except ValueError:
        print("Invalid ID or salary.")
        return

    if new_salary < 0:
        print("Salary cannot be negative.")
        return

    employee = find_employee_by_id(employees, employee_id)
    if employee is None:
        print("Employee not found.")
        return

    employee["salary"] = new_salary
    save_employees(employees)
    print("Salary updated successfully.")


def main():
    employees = load_employees()

    while True:
        print("\n===== Employee Data Management =====")
        print("1. Display all employees")
        print("2. Search by skill")
        print("3. Add employee")
        print("4. Update salary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            search_by_skill(employees)
        elif choice == "3":
            add_employee(employees)
        elif choice == "4":
            update_salary(employees)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()