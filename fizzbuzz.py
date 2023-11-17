n=int(input("Enter the end value of the range"))
for i in range(1,n+1):
    if (i%3==0 and i%5==0):
        print(i,"FIZZBUZZ")

    else:
        if i%5==0:
            print(i,"BUZZ")
        
        else:
            if (i%3==0):
                print(i,"FIZZ")
            
            else:
                print(i)