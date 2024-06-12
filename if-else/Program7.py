# Accept the marks of English, Math and Science,
# Social Studies Subject and display the stream allotted
# according to following:

# All Subjects more than 80 marks — Science Stream

# English >80 and Math, Science above 50 — Commerce Stream

# English > 80 and social studies > 80 — Humanities

studentName = input("Enter your name : ")
english = float(input("Enter marks in English: "))
math = float(input("Enter marks in Math: "))
science = float(input("Enter marks in Science: "))
social_studies = float(input("Enter marks in Social Studies: "))

# Determine the stream based on the marks
if english > 80 and math > 80 and science > 80 and social_studies > 80:
    stream = "Science Stream"
elif english > 80 and math > 50 and science > 50:
    stream = "Commerce Stream"
elif english > 80 and social_studies > 80:
    stream = "Humanities"
else:
    stream = "No stream meets the criteria"

print("The stream based on your marks is : ", stream)
    