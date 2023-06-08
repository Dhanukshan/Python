num1=int(input("enter start table:"))
b=int(input("enter last table:"))
for i in range(num1,b+1):
    for j in range(1,i+1):
        sum=i*j
        print(j,"*",i,"=",sum)
