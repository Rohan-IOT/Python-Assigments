age=int(input("Enter your age:"))
health_condition =input("Enter your health condition (smoker/non smoker):")
coverage_amount=int(input("Enter courage amount(in Rs):"))
if age >=25 and age <=44:
    base_premium=0.05*coverage_amount
elif age >=45 and age <=64:
    base_premium=0.06*coverage_amount
elif age >=65:
    base_premium=0.07*coverage_amount
else:
    print("Age is not in eligible range.")
    base_premium=0
if health_condition=="smoker":
    premium=base_premium*1.20
elif health_condition=="non smoker":
    premium=base_premium*0.90
else:
    print("Invalid Health condition")
    premium=0
if premium>0:
    print("The insurance premium is Rs.",premium)
