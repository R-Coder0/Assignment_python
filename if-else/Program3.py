# Accept the age of 4 people and display the youngest one?

# Accept ages of four people
age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: "))
age4 = int(input("Enter the age of the fourth person: "))

# Determine the youngest age using if-else statements
if age1 <= age2 and age1 <= age3 and age1 <= age4:
    youngest_age = age1
elif age2 <= age1 and age2 <= age3 and age2 <= age4:
    youngest_age = age2
elif age3 <= age1 and age3 <= age2 and age3 <= age4:
    youngest_age = age3
else:
    youngest_age = age4

# Display the youngest age
print("The youngest age is:",youngest_age)
