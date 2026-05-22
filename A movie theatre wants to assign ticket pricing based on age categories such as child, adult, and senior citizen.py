# A movie theatre wants to assign ticket pricing based on age categories such as child, adult, and senior citizen.

age = int(input("Enter the age of the person: "))
if age < 18:
    print("The ticket price is 100 rs for child .")
elif 18 <= age <= 65:
    print("The ticket price is 200 rs for adult .")
else:
    print("The ticket price is 150 rs for senior citizen.")

    #Output:

    """Enter the age of the person: 14
The ticket price is 100 rs for child ."""

    """Enter the age of the person: 25
The ticket price is 200 rs for adult ."""

    """Enter the age of the person: 87
The ticket price is 150 rs for senior citizen."""
