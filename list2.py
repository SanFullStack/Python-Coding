ages=[12,45,23,16,20,90,85,47,29,16,12,45,1,3,1,4,66,22,15]
print(ages.count(12))
print(len(ages))

ages.sort()
print(ages)

ages.reverse()
print(ages)

for age in ages:
    print(age)

for i in range(10):
    print(ages[i])

for i in range(10,0,-1):
    print(ages[i])

for i in range(len(ages),0,-1):
    print(ages[i])