import math
a=float(input("Enter the side of a triangle:"))
b=float(input("Enter the side of a triangle:"))
c=float(input("Enter the side of a triangle:"))
s=(a+b+c)/2.0
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)