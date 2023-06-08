a=int(input("enter first side of the triangle:"))
b=int(input("enter second side of the triangle:"))
c=int(input("enter third side of the triangle:"))
if(b*c==a*b+a*c):
    print("triangle is possible")
else:
    print("triangle is not possible")
