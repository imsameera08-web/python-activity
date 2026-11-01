print("===== WELCOME TO ATM =====")

balance = 5000

while True:
    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Select an option: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("Updated Balance:", balance)
        else:
            print("Enter a valid amount")

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 3:
        print("Your Current Balance:", balance)

    elif choice == 4:
        print("Thank you for using our ATM!")
        break

    else:
        print("Please select a valid option")