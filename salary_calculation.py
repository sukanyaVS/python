# Write a program that calculates an employee's monthly salary.
# Inputs:
# Basic salary
# HRA percentage
# DA percentage
# Tax percentage
 
# formula
# HRA = Basic Salary × HRA%
# DA = Basic Salary × DA%
# Gross Salary = Basic + HRA + DA
# Tax = Gross Salary × Tax%
# Net Salary = Gross Salary - Tax
 

basic_salary = float(input("Enter basic salary: "))
hra_percentage = float(input("Enter HRA percentage: "))
da_percentage = float(input("Enter DA percentage: "))
tax_percentage = float(input("Enter tax percentage: "))

hra = basic_salary * (hra_percentage / 100)
da = basic_salary * (da_percentage / 100)
gross_salary = basic_salary + hra + da
tax = gross_salary * (tax_percentage / 100)
net_salary = gross_salary - tax

print("Monthly Salary Details:")
print("------------------------")
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)