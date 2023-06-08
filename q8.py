name=input("enter name:")
age=int(input("enter age:"))
gender=input("enter gender:")
number_of_days=int(input("enter number of days:"))
if(age>=18 and age<=30):
    if(gender=='m'):
        wages=number_of_days*700
        print("Wages:",wages)
    else:
        wages=number_of_days*700
        print("Wages:",wages)
elif(age>=30 and age<=40):
    if(gender=='m'):
        wages=number_of_days*800
        print("Wages:",wages)
    else:
        wages=number_of_days*800
        print("Wages:",wages)
else:
    print("Invalid..!!")
