# Create a simple login program.
# Store:
# username = "admin"
# password = "Python@123"
# Ask the user to enter a username and password.
# The program should:
# Display "Login successful" if both are correct.
# Display "Invalid username" if the username is incorrect.
# Display "Invalid password" if the username is correct but password is incorrect.
# Display "Invalid username and password" if both are incorrect.
#  Allow the user a maximum of 3 login attempts

username = "admin"
password = "Python@123"

for attempts in range(3):

    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if (entered_username == username and entered_password == password):
        print("Login successful")
        break
    elif (entered_username != username and entered_password != password):
        print("Invalid username and password")
    elif (entered_username != username):
        print("Invalid username")
    else:
        print("Invalid password")
