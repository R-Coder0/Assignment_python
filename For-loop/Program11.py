# You have a nested list as below:
# indian_employees = [["Raj", "Patel"], ["Priya", "Sharma"],["Amit", "Kumar"],["Neha", "Singh"]]
# your have to create an email address for each employee.
# Email address should be there firstname+lastname@gmail.com

# Expected output:
# RajPatel@gmail.com
# PriyaSharma@gmail.com
# You have to create email addresses for each employee.


indian_employees = [["Raj", "Patel"], ["Priya", "Sharma"], ["Amit", "Kumar"], ["Neha", "Singh"]]

email_addresses = []

for employee in indian_employees:
    first_name = employee[0]
    last_name = employee[1]
    email = first_name + last_name + "@gmail.com"
    email_addresses.append(email)

# Print the email addresses
for email in email_addresses:
    print(email)
