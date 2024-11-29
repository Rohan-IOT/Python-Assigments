n=int(input("Enter a number:"))
s=" "
p=1
while n!=0:
    r=n%10
    if r!=0:
        s=str(r*p)+"+"+s
    n=n//10
    p=p*10
print(s,end='')

