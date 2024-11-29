n=int(input("Enter a number:"))
s=0
p=1
while n!=0:
    r=n%10
    s=s+r
    p=p*r
    n=n//10
if(s==p):
    print("It is a spy number")
else:
    print("It is not a spy number")

