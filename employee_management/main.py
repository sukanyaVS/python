from employee import (
    add_employee,
    display_employees,
    search_employee,
    update_employee,
    delete_employee,
    calculate_average_salary,
    find_employees_by_skill,
    find_experienced_employees
)

from exceptions import (
    DuplicateEmployeeError,
    EmployeeNotFoundError,
    InvalidSalaryError,
    InvalidExperienceError
)


def main():

    while True:

        print("\n================================")
        print("   Employee Resource Management")
        print("================================")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Calculate Average Salary")
        print("7. Find Employees By Skill")
        print("8. Find Experienced Employees")
        print("9. Exit")
        print("================================")

        choice = input(
            "Enter your choice (1-9): "
        ).strip()

        try:

            if choice == "1":
                add_employee()

            elif choice == "2":
                display_employees()

            elif choice == "3":
                search_employee()

            elif choice == "4":
                update_employee()

            elif choice == "5":
                delete_employee()

            elif choice == "6":
                calculate_average_salary()

            elif choice == "7":
                find_employees_by_skill()

            elif choice == "8":
                find_experienced_employees()

            elif choice == "9":
                print(
                    "Thank you for using "
                    "Employee Resource Management System."
                )
                break

            else:
                print(
                    "Invalid menu option. "
                    "Please choose between 1 and 9."
                )

        except ValueError:
            print(
                "Invalid input. "
                "Please enter the correct data type."
            )

        except DuplicateEmployeeError as error:
            print("Error:", error)

        except EmployeeNotFoundError as error:
            print("Error:", error)

        except InvalidSalaryError as error:
            print("Error:", error)

        except InvalidExperienceError as error:
            print("Error:", error)


if __name__ == "__main__": 
    main()