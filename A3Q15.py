a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
suma=0
sumb=0
for i in range(1,a):
    if(a%i==0):
        suma=suma+i
for j in range(1,b):
    if(b%j==0):
        sumb=sumb+j
if(suma==b and sumb==a):
    print("Number is amicable number.")
else:
    print("Number is not amicable number.")
