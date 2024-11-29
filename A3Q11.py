m=int(input("Enter the 1st number:"))
n=int(input("Enter the 2nd number:"))
ls=" "
while m!=0 and n!=0:
    r1=m%10
    r2=n%10
    ls=str(max(r1,r2))+ls
    m=m//10
    n=n//10
if m!=n:
    ls=str(max(m,n))+ls
print(ls)

