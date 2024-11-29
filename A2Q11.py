unit=int(input("Enter number of units consumed:"))
assert unit>=0
if unit <=100:
    bill=unit*3
elif unit<=200:
    bill=100*3+(unit-100)*4.80
elif unit <=400:
    bill=100*3+100*4.80+(unit-200)*5.80
else:
    bill=100*3+100*4.80+200*5.80+(unit-400)*6.20
online=input("Is the bill paid online ? (y/n):")
discount=0.0
if online =='y':
    discount=bill*0.03
else:
    print("No discount to be calculated",)
print("Total units consumed:",unit)
print("Bill amount:",bill)
print("Discount on bills:",discount)
print("Amount payable:",(bill-discount))
