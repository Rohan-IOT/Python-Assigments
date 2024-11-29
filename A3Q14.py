n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
print("The prime number in the range are:")
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)
