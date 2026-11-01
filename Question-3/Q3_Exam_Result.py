
print("===== EXAMINATION RESULT =====")

total = 0
failed = 0

for i in range(1, 6):
    marks = int(input("Enter subject marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
        failed = failed + 1

    elif marks >= 30 and marks < 35:
        marks = 35
        total = total + marks

    elif marks < 35:
        failed = failed + 1
        total = total + marks

    else:
        total = total + marks

print("Total Marks:", total)

if failed == 0:
    print("Result: PASS")
else:
    print("Result: FAIL")