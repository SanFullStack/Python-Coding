import random
def choose():
    List=[junglebook,titanic,dearzindagi,deshdrohi,stree,fan,tamasha,thappad,sexeducation]
    secret=random.choice(list)
    return secret

def moviename():
    p1name=input("Player 1 please enter your name :")
    p2name=input("Player 2 please enter your name :")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if (turn%2==0):
            print(p1name," its your turn : ")
            picked_movie=random.choice(List)
            qn=create_question(picked)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Enter the letter : ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modifeid_qn,picked_movie,ch)
                    print(modified_qn)
                    d=input("PRess 1 to guess the movie name or 2  to unlock anpther letter :")
                    if d==1:
                        ans=input("Your answer : ")
                        if (ans==picked_movie):
                            pp1=pp1+5
                            print("Correct")
                            not_said=False
                            print(p1name," your score is ",pp1)
            
                else:
                    print (letter," not found ")
            c=input("Press 1 to continue or 0 to quit : ")
            if (c==0):
                print(pp1,pp2)
                willing=False
                

        else:
            turn=turn+1
      
        else:
            print(p2name," its your turn : ")
            picked_movie=random.choice(List)
            qn=create_question(picked)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Enter the letter : ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modifeid_qn,picked_movie,ch)
                    print(modified_qn)
                    d=input("Press 1 to guess the movie name or 2  to unlock anpther letter :")
                    if d==1:
                        ans=input("Your answer : ")
                        if (ans==picked_movie):
                            pp2=pp2+5
                            print("Correct")
                            not_said=False
                            print(p2name," your score is ",pp2)

                else:
                    print (letter," not found ")


    else:
play()
                    
