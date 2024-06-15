# Write a Python program to print the multiplication table of a given number using a for loop.
number = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{number} X {i} = {number * i}")