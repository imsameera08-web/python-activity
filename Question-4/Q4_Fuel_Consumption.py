
print("===== FUEL COST COMPARISON =====")

distance = float(input("Enter distance in km: "))
price = float(input("Enter fuel price per litre: "))

mileage1 = float(input("Enter mileage of vehicle 1: "))
mileage2 = float(input("Enter mileage of vehicle 2: "))

if distance > 0 and price > 0 and mileage1 > 0 and mileage2 > 0:

    fuel1 = distance / mileage1
    fuel2 = distance / mileage2

    cost1 = fuel1 * price
    cost2 = fuel2 * price

    print("\nVehicle 1 Fuel Cost:", cost1)
    print("Vehicle 2 Fuel Cost:", cost2)

    if cost1 < cost2:
        print("Vehicle 1 is cheaper")
    elif cost2 < cost1:
        print("Vehicle 2 is cheaper")
    else:
        print("Both vehicles have equal cost")

else:
    print("Enter valid positive values")