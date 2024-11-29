import random
acc_bal=random.randint(1,10000)
print("Available balance:",acc_bal)
trans_amt=int(input("Enter the amount:"))
if(trans_amt<acc_bal):
    bal=acc_bal-trans_amt
    print("Remaining balance:",bal)
elif(acc_bal<trans_amt):
    print("Insufficient Amount")
else:
    print("Invalid Transaction")
    
