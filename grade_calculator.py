# Create a function:
# calculate_grade(marks)
# The function should accept marks and return:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# 50–59  → E
# Below 50 → F


def calculate_grade(mark):

    match mark:
        case mark if 90 <= mark <= 100:
            return "A"
        case mark if 80 <= mark <= 89:
            return "B"
        case mark if 70 <= mark <= 79:
            return "C"
        case mark if 60 <= mark <= 69:
            return "D"
        case mark if 50 <= mark <= 59:
            return "E"
        case _:
            return "F"

mark = int(input("Enter mark: "))
grade = calculate_grade(mark)
print("Grade:", grade)
