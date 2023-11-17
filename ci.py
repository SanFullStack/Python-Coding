import math
p=float(input("Enter the principle : "))
r=float(input("Enter the rate : "))
t=int(input("Enter the time : "))
n=int(input("Enter the no of times the interest applied per period : "))
a=p*(math.pow((1+(r/n)),(n*t)))
print(a)
