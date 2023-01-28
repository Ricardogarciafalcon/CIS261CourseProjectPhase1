def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) /100)
    net_pay = float(total_hours) * float(hourly_rate) - tax
    return tax, net_pay

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetHoursWorked():
    Hours_Worked = float(input("Enter total hours: "))
    return Hours_Worked

def GetHourlyRate():
    Hourly_Rate = float(input("Enter hourly rate: "))
    return Hourly_Rate

def GetTaxRate():
    Tax_rate = float(input("Enter tax rate (in %): "))
    return tax_rate
   

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    print("Hourly rate: ", {hourly_rate})
    print("Gross pay: ", {gross_pay})
    print("Tax rate: ", {tax_rate})
    print("Income tax: ", {tax})
    print("Net pay: ", {net_pay})

    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print(f"Total Gross pay: {TotGrossPay}")
    print(f"Total Net pay: {TotNetpay:,.2f}")
    print(f"Total Tax: {TotTax}")


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        Hours = total_hours()
        GetHourlyRate = hourly_rate()
        GetTaxRate = tax_rate()
        gross_pay = gross_pay(hours, hourly_rate)
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotTax += tax
        TotGrossPay += gross_pay
        TotNetPay += net_pay

    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
