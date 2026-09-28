# Create a generator function filter_text() that yields only records containing a specified keyword.

def filter_text(keyword, records):
    for record in records:
        if keyword.lower() in record.lower():
            yield record

records = ["I love Python", "Java is great", "Python is powerful", "Angular is a frontend framework", "Python supports generators"]
keyword = input("Enter a keyword to filter records: ")           

filtered_records = filter_text(keyword, records)

for record in filtered_records:
    print(record)
