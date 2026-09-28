# Create a generator function clean_text() that receives the records and:
# Removes unnecessary spaces.
# Converts text to lowercase.
# Removes empty records.


def clean_text(records):
    for record in records:
        record = record.strip().lower()
        if record:
            yield record

records = ["  I love Python  ", "Java is great", "  ", "Python is powerful", "  Angular is a frontend framework", "Python supports generators"]

for record in records:
    print(f"Original: '{record}'")

print("=================================")    

for record in clean_text(records):
    print(f"Cleaned: '{record}'")