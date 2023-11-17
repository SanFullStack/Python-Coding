import random

def play():
    p1name=input("Player 1 please enter your name : ")
    p2name=input("Player 2 please enter your name : ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if (turn%2==0):
            print(p1name," Its your turn :) ")
            ans=input("Can you guess the correct word ? ")
            if (ans==picked_word):
                pp1=pp1+5
                print("your score is : ",pp1)
            else:
                print("better luck next time :) ")
                c=int(input("press 1 if you want to continue or press 0 if you want to quit : "))
                if (c==0):
                    thank(p1name,p2name,pp1,pp2)
                    break
            
        else:
            print(p2name," Its your turn :) ")
            ans=input("Can you guess the correct word ? ")
            if (ans==picked_word):
                pp2=pp2+5
                print("Your score is : ",pp2)
            else:
                print("Better luck next time :) ")
                c=int(input("Press 1 if you want to continue or press 0 if you want to quit : "))
                if (c==0):
                    thank(p1name,p2name,pp1,pp2)
                    break

        turn=turn+1
play()

def choose():
    word=["bread","watermelon","hydration","photosynthesis","brinjal","pumpkin","balloon","hibiscus","draognfly","player"]
    pick=random.choice(word)
    return pick

def jumble(word):
    jumbled=" ".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n, "Your score is : ", p1)
    print(p2n, "Your score is : ", p2)
    if(p1>p2):
        print(p1n, "Is the winner :) :) :) ")

    else:
        print(p2n, "Is the winner :) :) :) ")

    print("Thank you both for playing the game ")