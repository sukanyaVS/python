# Create a list of text records containing at least 10 sentences .Use a list comprehension with a condition to extract only words whose length is greater than 4 characters.

records = [
    "Python is easy to learn",
    "JavaScript is widely used",
    "Angular is a frontend framework",
    "React makes building interfaces easier",
    "Developers write clean code",
    "Functions help organize programs",
    "Generators produce values one by one",
    "Lists can store multiple values",
    "Dictionaries contain keys and values",
    "Exception handling prevents program crashes"
]

new_list = [words for record in records for words in record.split() if len(words) > 4]
print(new_list)

# Create a list of text records containing at least 10 sentences.Create a dictionary containing only words whose length is greater than 5 characters.

new_dict = {words: len(words) for record in records for words in record.split() if len(words) > 5}
print(new_dict)
