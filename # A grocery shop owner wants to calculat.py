# A grocery shop owner wants to calculate the final bill after applying discounts based on the purchase amount.
# Write a program using if...elif...else to display the final amount.

purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount < 100:
    final_bill = purchase_amount
elif purchase_amount < 500:
    final_bill = purchase_amount - (purchase_amount * 0.1)  
else:
    final_bill = purchase_amount - (purchase_amount * 0.2)  

print("Final bill amount:", final_bill)
