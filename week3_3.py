n=int(input("Enter the last limit of the array : "))
l=list(map(int,input().split()))
s=l[0]
print(s,end=" ")
for i in l:
    if(s!=i):
        print(i,end=" ")

