a=int(input("Enter the no of red candies"))
b=int(input("Enter the no of blue candies"))
if a<b:
    smaller=a
else:
    smaller=b

for i in range(1,smaller+1):
    if((a%i==0)and(b%i==0)):
        hcf=i

print(hcf)
