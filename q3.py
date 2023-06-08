speed=int(input("enter wind speed in kilometers per hour="))
temp=int(input("enter temperature in degree celsius="))
t=temp
v=speed
wci=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
windchillindex=round(wci)
print("wind chill index=",windchillindex)
