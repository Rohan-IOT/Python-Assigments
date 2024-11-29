purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount <= 100:
        discount_rate = 0
elif purchase_amount <= 500:
        discount_rate = 0.05  # 5%
elif purchase_amount <= 1000:
        discount_rate = 0.10  # 10%
else:
        discount_rate = 0.15  # 15%
discount = purchase_amount * discount_rate
final_amount = purchase_amount - discount
print("Purchase Amount: ",purchase_amount)
print("Discount:",discount)
print("Final Amount after Discount:",final_amount)
