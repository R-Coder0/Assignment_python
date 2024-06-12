# Write a Python program to count the number of even and odd numbers from a series of numbers using a for loop.
numbers = [50, 70, 56, 65, 98, 73, 71, 69, 54]

even_count= 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Number of even numbers : {even_count}")
print(f"Number of odd numbers : {odd_count}")