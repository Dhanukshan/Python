year=int(input("enter the year:"))
if(year/400==0):
    print("it is an leap year")
elif(year/100==0):
    print("it is not an leap year")
elif(year/4==0):
    print("it is an leap year")
else:
    print("it is not an leap year")
