print("===== SMART CANTEEN =====")

tea_stock = 20
coffee_stock = 15
sandwich_stock = 10

total = 0

while True:
    print("\n1. Tea - Rs.10")
    print("2. Coffee - Rs.20")
    print("3. Sandwich - Rs.40")
    print("4. Exit")

    choice = int(input("Select your item: "))

    if choice == 1:
        quantity = int(input("Enter quantity: "))

        if quantity > 0 and quantity <= tea_stock:
            total = total + quantity * 10
            tea_stock = tea_stock - quantity
            print("Tea ordered successfully")
        else:
            print("Tea is unavailable or quantity is invalid")

    elif choice == 2:
        quantity = int(input("Enter quantity: "))

        if quantity > 0 and quantity <= coffee_stock:
            total = total + quantity * 20
            coffee_stock = coffee_stock - quantity
            print("Coffee ordered successfully")
        else:
            print("Coffee is unavailable or quantity is invalid")

    elif choice == 3:
        quantity = int(input("Enter quantity: "))

        if quantity > 0 and quantity <= sandwich_stock:
            total = total + quantity * 40
            sandwich_stock = sandwich_stock - quantity
            print("Sandwich ordered successfully")
        else:
            print("Sandwich is unavailable or quantity is invalid")

    elif choice == 4:
        print("\n===== BILL =====")
        print("Total Amount: Rs.", total)
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice")