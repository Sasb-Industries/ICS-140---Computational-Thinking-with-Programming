hourlyRate = float(input("Enter the hourly rate : "))
hoursWorked = float(input("Enter the hours worked : "))
overtimeRate = hourlyRate * 1.5

if hoursWorked < 0:
    print("Enter a legitimate number you BOZO")
elif hoursWorked <= 40:
    regularPay = round((hourlyRate * hoursWorked),2)
    print("Regular hours : ",hoursWorked)
    print("Regular pay : $", regularPay)
elif hoursWorked > 40:
    regularPay = round((hourlyRate * 40),2)
    overtimeHours = hoursWorked - 40
    overtimePay = round((overtimeHours * overtimeRate),2)
    totalPay = regularPay + overtimePay
    print("Regular hours : 40")
    print("Regular pay : $", regularPay)
    print("Overtime hours : ",overtimeHours)
    print("Overtime pay : $",overtimePay)
    print("Total pay : $",totalPay)
else:
    print("It's Boken")
