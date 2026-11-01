
print("===== RETAIL BILLING =====")

total = 0
n = int(input("Enter number of products: "))

for i in range(n):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    total = total + price * quantity

print("Total Amount:", total)

if total >= 5000:
    discount = total * 0.20
elif total >= 2000:
    discount = total * 0.10
else:
    discount = 0

if discount > 1000:
    discount = 1000

final_amount = total - discount

print("Discount:", discount)
print("Final Bill:", final_amount)