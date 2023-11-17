l=list(map(int,input().split()))
a=max(l)
print(a)
b=min(l)
print(b)
sa=sb=l[0]
for i in l:
    if(i!=sa):
        if(i!=a and i!=b):
            if(sa<i):
                sa=i
            elif(sb>i):
                sb=i

print(sa)
print(sb)
print(sa+sb)