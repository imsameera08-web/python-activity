print("===== EMPLOYEE PAYROLL =====")

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime amount: "))

gross = basic + allowance + overtime

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

salary = gross - deduction

print("\nEmployee Name:", name)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", salary)