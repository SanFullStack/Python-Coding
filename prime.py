n=int(input("Enter a number : "))
c=0
p=n//2
for i in range(2,p+1):
    if n%i==0:
        c=c+1

if(c==0):
    print("Prime")

else:
    print("Not prime")