# Write a program to calculate the electricity bill
# using only if statement? (accept number of unit from user)
# according to the following criteria:

# Unit Price
# First 100 units no charge
# Next 100 units Rs 5 per unit
# After 200 units Rs 10 per unit

units = int(input("Enter the number of unit consume:"))

#initialize the bill amount..
bill_amount = 0

#calculate the bill on the base of unit consume
if units <= 100:
    bill_amount = 0
elif units <= 200:
    bill_amount = (units-100) * 5
else:
    bill_amount = (100 * 5) + ((units-200)*10)
print("The total bill amount is:", bill_amount)