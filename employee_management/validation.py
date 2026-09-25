from exceptions import InvalidSalaryError, InvalidExperienceError


def validate_name(name):
    name = name.strip()

    if not name:
        raise ValueError("Employee name cannot be empty.")

    return name


def validate_salary(salary):
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

    return salary


def validate_experience(experience):
    if experience < 0:
        raise InvalidExperienceError("Experience cannot be negative.")

    return experience