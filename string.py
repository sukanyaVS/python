# Ask the user to enter their full name.
# Example:
# Input:   anu   maria   joseph
# Output:  Anu Maria Joseph
# Program should:
# Remove unnecessary spaces.
# Convert the name into proper title case.
# Display the first name.
# Display the last name.
# Display the initials.

full_name = input("Enter your full name: ")
full_name = full_name.strip()
full_name = " ".join(full_name.split())
full_name = full_name.title()

first_name = full_name.split()[0]

last_name = full_name.split()[-1]

initials = ""

for name in full_name.split():
     initials = initials + name[0]

print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Initials:", initials)