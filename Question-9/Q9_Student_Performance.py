print("===== STUDENT PERFORMANCE =====")

name = input("Enter student name: ")

m1 = int(input("Enter first exam marks: "))
m2 = int(input("Enter second exam marks: "))
m3 = int(input("Enter third exam marks: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 75:
    print("Performance: Excellent")
elif average >= 50:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")

if m3 > m2:
    print("Performance is improving")
elif m3 < m2:
    print("Performance is decreasing")
else:
    print("Performance is unchanged")