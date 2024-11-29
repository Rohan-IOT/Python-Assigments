emp=input("Enter employees position:")
sal=int(input("Enter the salary of the employee:"))
yrs=int(input("Enter the year of service of the employee:"))
total=sal*yrs
bonus=0
if emp=='manager' and yrs>5:
    bonus=(yrs-5)*sal*0.1
elif emp=='engineer' and yrs>3:
    bonus=(yrs-3)*sal*0.05
print("Salary statement of",emp)
print("Income from salary",total)
print("Bonus",bonus)
print("Total income",(total+bonus))
