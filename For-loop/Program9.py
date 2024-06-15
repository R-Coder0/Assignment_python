# Write a Python program to reverse a given string using a for loop.
string = input("Enter the string which you want to reverse : ")

reversed_string = ""

for char in string[::-1]:
    reversed_string += char
    
print("Reversed String : ", reversed_string)