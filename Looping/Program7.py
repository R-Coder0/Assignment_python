# Write a Python program to check if a given number is prime or not using a for loop.

number = int(input("Enter the number : "))

is_prime = True

if number > 1:
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
        
else:
    is_prime = False

if is_prime:
    print(number ,"is a prime number.")
else:
    print(number ,"is not a prime number.")            