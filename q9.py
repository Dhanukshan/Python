food=int(input("enter food rating:"))
service=int(input("enter service rating:"))
ambience=int(input("enter ambience rating:"))
bill=int(input("enter bill amount:"))
if(food==4 or food==5):
    if(service==4 or 5 and ambience==4 or 5):
        tip=bill*0.1
        print("Tip:",tip)
    else:
        tip=bil*0.05
        print("Tip:",tip)
else:
    if(service==4 or 5 and ambience==4 or 5):
        tip=bill*0.05
        print("Tip:",tip)
    else:
        tip=bil*0.01
        print("Tip:",tip)
