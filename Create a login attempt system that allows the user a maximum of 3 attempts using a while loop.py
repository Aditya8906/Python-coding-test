# Create a login attempt system that allows the user a maximum of 3 attempts using a while loop.
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # For demonstration purposes, let's assume the correct username and password are "admin" and "password123"
    if username == "Coding" and password == "Test":
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Login failed and  You have {max_attempts - attempts} attempts left.")

# Output:
"""Enter username: Coding 
Enter password: Test
Login successful!"""

"""Enter username: code
Enter password: test
Login failed and  You have 2 attempts left."""