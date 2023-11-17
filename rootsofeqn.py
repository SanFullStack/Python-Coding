import math
a=float(input("Enter a no"))
b=float(input("Enter a no"))
c=float(input("Enter a no"))
dis=b*b-(4.0*a*c)
if dis>0.0:
    r1=(-b+math.sqrt(dis))/(2.0*a)
    r2=(-b-math.sqrt(dis))/(2.0*a)
    print("The first root is : ",r1)
    print("The second root is : ",r2)

elif dis==0.0:
    r1=(-b)/(2.0*a)
    print("both the roots are equal")
    print(" the first and second roots are : ",r1) 

else:
    print("no roots are equal . the roots are imaginary")       
