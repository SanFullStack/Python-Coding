n=int(input("enter the electricity bill : "))
if (n<=100):
    b=n*50

elif (n<=200):
    b=120+((n-100)*1.25)

elif (n<=300):
    b=250+((n-200)*2.25)

elif (n<=400):
    b=300+((n-300)*3.25)

else:
    b=400+((n-400)*4.25)

print(b)    