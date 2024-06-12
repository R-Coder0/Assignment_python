# Write a program to display "Hello" if a number entered
# by user is a multiple of five, otherwise print "Bye"?

number = int(input("Enter the number : "))

if (number % 5) == 0:
    print("hello")
else:
    print("Bye!!")