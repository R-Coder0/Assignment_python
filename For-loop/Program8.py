# Write a Python program to find the largest element in a list using a for loop.

numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers
numbers = [int(num) for num in numbers]

max_number = numbers[0]

for num in numbers[1:]:
    if num > max_number:
        max_number = num

print("The largest element in the list is:", max_number)
