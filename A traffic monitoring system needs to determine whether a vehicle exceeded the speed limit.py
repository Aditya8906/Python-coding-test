# A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit.

speed_limit = 60
speed = int(input("Enter the speed of the vehicle: "))
if speed > speed_limit:
    print("The vehicle exceeded the speed limit.")
else:
    print("The vehicle did not exceed the speed limit.")

# Output:

"""Enter the speed of the vehicle: 48
The vehicle did not exceed the speed limit."""

"""Enter the speed of the vehicle: 89
The vehicle exceeded the speed limit."""

