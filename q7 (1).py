salary=int(input("enter current salary:"))
work=int(input("enter years of services:"))
if(work>10):
    bonus=salary*0.1
    print("Bonus:",bonus)
elif(work<=10 and work>6):
    bonus=salary*0.8
    print("Bonus:",bonus)
else:
    bonus=salary*0.05
    print("Bonus:",bonus)
