shopping = ["bread" , "coffee" , "tea" ,"muffin"]

#way to print the list using the list name without braces and colons
for i in shopping:
    print(i)

#way to print the list in bracket format
print(shopping)

#append function adds values to the end of the list
#and the function append takes only one argument

shopping.append("curd")

print(shopping)

#way to print the list without braces and colons using for loop
for i in range(5):
    print(shopping[i])

#the insert function helps in inserting or adding values or items in the desired position

shopping.insert(1,"oil")
shopping.insert(3,"shampoo")

print(shopping)

for item in shopping:
    print(item)

for i in range(7):
    print(shopping[i])


