# Write a program to accept percentage from the user and display
# the grade according to the following criteria:

# Marks Grade
# > 90 A
# > 80 and <= 90 B
# >= 60 and <= 80 C
# below 60 D

student_name = input("Enter Your Name:")
marks_obtained = int(input("Enter the marks_obtained:"))
Grade = 0

if marks_obtained > 90:
    Grade = "A"
elif marks_obtained > 80 and marks_obtained <= 90 :
    Grade = "B"
elif marks_obtained >= 60 and marks_obtained <=80:
    Grade = "C"
elif marks_obtained >=40 and marks_obtained <60:
    Grade = "D"
else:
    Grade = "Fail"
print("Name : ", student_name)
print("Marks Obtained : ", marks_obtained)
print("Grade : ",Grade)