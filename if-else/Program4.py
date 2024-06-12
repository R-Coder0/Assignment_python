# A company decided to give bonus to employee
# according to following criteria:
# Time period of Service Bonus
# More than 10 years 10%
# >=6 and <=10 8%
# Less than 6 years 5%
# Ask user for their salary and years of service and print the
# net bonus amount?
import math

employeeName = input("Enter your name :")
employeeSalary = int(input("Enter your current salary : "))
timePeriod  = int(input("Enter your employee period : "))
netBounus = 0

if timePeriod >= 10:
    netBounus = (employeeSalary * 10) /  100
elif timePeriod >= 6 and timePeriod <= 10 :
    netBounus = (employeeSalary * 8)/100
elif timePeriod < 6:
    netBounus = (employeeSalary  * 5)/100
else:
    netBounus = (employeeSalary * 3)/100
print("Employee Name: ", employeeName)
print("Employee Salary: ", employeeSalary)
print("Employee TimePeriod : ", timePeriod)
print("Employee Bonus: ", netBounus)