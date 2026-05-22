# Create a program to check whether a given username and password match predefined credentials. 

predefined_username = "admin"
predefined_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == predefined_username and password == predefined_password:
    print("Access granted")
else:
    print("Access denied")

# Output:
"""Enter username: admin
Enter password: password123
Access granted"""

"""Enter username: Asm
Enter password: ut98
Access denied"""
