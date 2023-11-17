numbers=[2,3,5,4,7,12,14,13,24,40,14]
print(numbers)
#a=[int(i) for i in input().split()]
a=list(map(int,input().split()))
for i in a:
    if(i%10!=4):
        print(i, end=" ")