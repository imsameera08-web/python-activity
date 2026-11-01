
print("===== RAILWAY TICKET BOOKING =====")

name = input("Enter passenger name: ")
age = int(input("Enter age: "))
distance = float(input("Enter distance in km: "))

if distance <= 100:
    fare = distance * 1
elif distance <= 300:
    fare = distance * 1.5
else:
    fare = distance * 2

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.7

fare = fare + 50

print("\nPassenger:", name)
print("Ticket Fare:", fare)
print("Reservation charge: Rs.50")