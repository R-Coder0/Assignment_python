# Write a program to check whether a number entered
# is three-digit number or not?

number = int(input("Enter the number : "))

if  100 <= abs(number)  <= 999:
    print(f"The number {number} is a three-digit number.")
else:
    print(f"The number {number} is not three-digit number.")