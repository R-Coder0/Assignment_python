# Write a Python program to print the Fibonacci sequence up to a specified number using a for loop.

limit = int(input("Enter the limit of series : "))

a , b = 0 , 1

print("Fibonacci sequence up to", limit, ":")
for i in range(limit):
    print(a, end=" ")
    a, b = b, a + b