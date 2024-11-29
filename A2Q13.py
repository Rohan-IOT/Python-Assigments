'''t1=input("Enter am or pm:")
t2=float(input("Enter time here:"))
if(t1=='am' and t2<= 12):
   print("Time is:",12)
elif(t1=='pm' and t2<= 12):
     print("Time is:",(t2+t2))
else:
    print("Invalid")'''

hrs=int(input("Enter the hours(1-12):"))
mins=int(input("Enter the minutes(0-59):"))
period=input("Enter the period(AM/PM):")
if hrs<1 or hrs>12:
   print("Invalid hours")
elif mins<0 or mins>59:
   print("Invalid minutes")
else:
   if period=="PM" and hrs!=12:
      hrs+=12
   elif period=="AM" and hrs==12:
      hrs=0
   if hrs<10:
      hrs_str="0"+str(hrs)
   else:
      hrs_str=str(hrs)
   if mins<10:
      mins_str="0"+str(mins)
   else:
      mins_str=str(mins)
   print("Time in 24 hours format:",hrs_str,":",mins_str)
    
