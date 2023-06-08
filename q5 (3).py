num1=int(input("enter start table:"))
num2=int(input("enter stop table:"))
for i in range(num1,num2+1):
    for j in range(1,10+1):
        sum=i*j
        print(j,"x",i,"=",sum)
