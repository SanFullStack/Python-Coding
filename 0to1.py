import random

def choose():
    binary_number=[0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1]
    pick=random.choice(binary_number)
    return pick()

def convert():
    picked_number=choose()
    if (picked_number==0):
        picked_number=1   
    
def display():
    convert()
    print(binary_number)

display()