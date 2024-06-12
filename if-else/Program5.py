# Accept three numbers from the user and
# display the second largest number?

firstNumber = int(input("Enter your first number :"))
secondNumber = int(input("Enter your second number :"))
thirdNumber = int(input("Enter your third number :"))

# Determine the second largest number using if-else statements
if (firstNumber > secondNumber):
    if (firstNumber > thirdNumber):
        if (secondNumber > thirdNumber):
            second_largest = secondNumber
        else:
            second_largest = thirdNumber
    else:
        second_largest = firstNumber
else:
    if (secondNumber > thirdNumber):
        if (firstNumber > thirdNumber):
            second_largest = firstNumber
        else:
            second_largest = thirdNumber
    else:
        second_largest = secondNumber

print("The second largest number is:", second_largest)
