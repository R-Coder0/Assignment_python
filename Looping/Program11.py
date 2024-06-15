# You have a nested list as below:
# indian_employees = [["Raj", "Patel"], ["Priya", "Sharma"],["Amit", "Kumar"],["Neha", "Singh"]]
# your have to create an email address for each employee.
# Email address should be there firstname+lastname@gmail.com

# Expected output:
# RajPatel@gmail.com
# PriyaSharma@gmail.com
# You have to create email addresses for each employee.

indian_employees = [["Raj", "Patel"], ["Priya", "Sharma"], ["Amit", "Kumar"], ["Neha", "Singh"]]

for employee in indian_employees:
    email = "{}{}@gmail.com".format(employee[0].lower(), employee[1].lower())
    print(email)
