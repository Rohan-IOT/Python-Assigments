import math
n=int(input("Enter the degree:"))
x=math.radians(n)
i=3
term=x
tsum=x
while abs(term)>10**-6:
    term=-(term*x**2/(i*(i-1)))
    tsum=tsum+term
    i=i+2
print("Sin(n)=",tsum)
