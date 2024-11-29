n=int(input("Enter a number:"))
c=n
f=h=x=0
for i in range(2,n):
    if n%i==0:
        f=1
        break
while(n>0):
    x=x*10+n%10
    n=n//10
for i in range(2,x):
    if x%i==0:
        h=1
        break
if f==0 and h==0:
    print("Twisted prime")
else:
    print("Not twisted prime")
    
