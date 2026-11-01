
print("===== TRAFFIC FINE CALCULATOR =====")

print("1. Over Speeding")
print("2. No Helmet")
print("3. Signal Jumping")

choice = int(input("Enter violation number: "))

if choice == 1:
    fine = 1000
    print("Violation: Over Speeding")

elif choice == 2:
    fine = 500
    print("Violation: No Helmet")

elif choice == 3:
    fine = 1500
    print("Violation: Signal Jumping")

else:
    fine = 0
    print("Invalid choice")

print("Penalty Amount: Rs.", fine)
