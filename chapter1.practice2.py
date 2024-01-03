import math
x=int(input("Enter the value of x : "))
y=int(input("Enter the value of Y : "))
res=2*math.cos((x+y)/2)*math.cos((x-y)/2)+math.exp(x)-1-(x/4)+math.tan(x)-math.log(y)
print(res)
"""
Mtah Module is Used For
math.cos()
masth.sin()
math.tan()
math.exp()
math.pow(x,y)
math.radinas()
math.pi
math.degrees(radians_value)
"""