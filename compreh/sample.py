# List

numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]

print(squares)    

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
greater_than_five = [number for number in numbers if number > 5]
print(greater_than_five)

# Dictionary

numbers = [1, 2, 3, 4, 5]
squares = {number: number * number for number in numbers}
print(squares)

result = {number: number * number for number in numbers if number > 2}

print(result)

employees = {
    "John": 50000,
    "Alice": 60000,
    "Bob": 45000,
    "David": 70000
}

new_array = {name: salary for name, salary in employees.items() if salary > 50000}
print(new_array)

# Set

print("===================")
numbers = [1, 2, 2, 3, 3, 4, 5]
squares_list = [number * number for number in numbers]
print(squares_list)
squares_set = {number * number for number in numbers}
print(squares_set)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_set = {number * number for number in numbers if number % 2 == 0}
print(new_set)