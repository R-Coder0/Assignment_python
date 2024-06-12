# Write a program to check whether the last digit of a number
# (entered by user) is divisible by 3 or not?

number = float(input("Enter the number : "))

last_digit = number % 10

if last_digit % 3 == 0:
    print(f"The last digit of the number {number} is {last_digit} and it is divisible by 3.")
else:
    print(f"The last digit of the number {number} is {last_digit} and it is not divisible by 3.")