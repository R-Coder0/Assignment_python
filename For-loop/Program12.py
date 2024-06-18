# Write a Python program that generates a random number between 1 and 100. The user should then repeatedly guess the number until they guess it correctly. After each guess, the program should provide feedback to the user, indicating whether their guess is too high, too low, or correct. Once the correct number is guessed, the program should print the number of attempts it took the user to guess the correct number.

import random 

def guessing_number():
    
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    guess = None
    
    print("Welcome to the number guessing number game!!")
    print("I have selected a random nuumber between 1 to 100. You have to guess the number")
    
    while guess != target_number and attempts < max_attempts: 
        guess = int(input("Enter the number : "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! try again.")
        elif guess > target_number:
            print("Too high! try again.")
        else:
            print(f"Congratulation !! You have guess the correct number {target_number} in {attempts} attempts.")
    if guess != target_number:
        print(f"sorry, you have use your all attempts. The number is {target_number} ")

            
guessing_number()