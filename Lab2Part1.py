#Eddy Guzman
#Lab2-Part1
efirstName = input("Employee first name: ")
elastName = input("Employee last name: ")
eID = int(input("Enter ID number: "))
hoursWorked = int(input("Enter hours worked: "))
ePay = float(input("Enter pay rate: "))

grossPay = ePay * hoursWorked
tax = grossPay * 0.2;
netPay = grossPay - tax

print("\nName:", elastName, ",", efirstName)
print("Hours:", hoursWorked)
print("Pay Rate: $", "{:.2f}".format(ePay))
print("Gross Pay: $", "{:.2f}".format(grossPay))
print("Tax Deduction: $", "{:.2f}".format(tax))
print("Net Pay: $", "{:.2f}".format(netPay))

# Eddy Guzman
# Lab2-Part2
#def computeTax(gross):
#    tax = 0.2*gross
#    return tax
#def computeNetPay(gross):
#    tax = computeTax(gross)
#    netPay = gross - tax
#    return netPay

#efirstName = input("Employee first name: ")
#elastName = input("Employee last name: ")
#eID = int(input("Enter ID number: "))
#hoursWorked = int(input("Enter hours worked: "))
#ePay = float(input("Enter pay rate: "))

#grossPay = ePay * hoursWorked
#tax = computeTax(grossPay)
#netPay = computeNetPay(grossPay)

#print("\nName:", elastName, ",", efirstName)
#print("Hours:", hoursWorked)
#print("Pay Rate:", ePay)
#print("Gross Pay:", grossPay)
#print("Tax Deduction:", tax)
#print("Net Pay:", netPay)

#Eddy Guzman
#Lab2Part3
#def computeTaxNetPay(grossPay):
#   global tax
#    tax = 0.2 * grossPay
#    global netPay
#    netPay = grossPay - tax

#efirstName = input("Employee first name: ")
#elastName = input("Employee last name: ")
#eID = int(input("Enter ID number: "))
#hoursWorked = int(input("Enter hours worked: "))
#ePay = float(input("Enter pay rate: "))

#grossPay = ePay * hoursWorked
#computeTaxNetPay(grossPay)

#print("\nName:", elastName, ",", efirstName)
#print("Hours:", hoursWorked)
#print("Pay Rate: $", "{:.2f}".format(ePay))
#print("Gross Pay: $", "{:.2f}".format(grossPay))
#print("Tax Deduction: $", "{:.2f}".format(tax))
#print("Net Pay: $", "{:.2f}".format(netPay))




