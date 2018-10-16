# tic tac too
import os
from random import choice
print('\n\nPress a number to place your turn\nYour choice is ' 'X\n')
s=[0,0]
while True:
    l=['_','_','_','_','_','_','_','_','_']
    #    0   1   2   3   4   5   6   7   8 
    lc=[0,1,2,3,4,5,6,7,8]
    print(l[6],l[7],l[8],"\t\t7  8  9") 
    print(l[3],l[4],l[5],"\t\t4  5  6")
    print(l[0],l[1],l[2],"\t\t1  2  3")
    while True:
        x=int(input("\n\nEnter "))
        os.system('cls')
        l[x-1]='X'
        lc.remove(x-1)
        if lc.__len__()!=0:
            com=choice(lc)
            l[com]="O"
            lc.remove(com)
        print(l[6],l[7],l[8],"\t\t7  8  9\t\t Score") 
        print(l[3],l[4],l[5],"\t\t4  5  6\t\t C   U")
        print(l[0],l[1],l[2],"\t\t1  2  3\t\t",s[0]," ",s[1])
        if (l[6]==l[3]==l[0]=='O') or (l[7]==l[4]==l[1]=='O') or (l[8]==l[5]==l[2]=='O') or (l[6]==l[7]==l[8]=='O') or (l[4]==l[3]==l[5]=='O') or (l[2]==l[1]==l[0]=='O') or (l[6]==l[2]==l[4]=='O') or (l[8]==l[4]==l[0]=='O') :
            print('computer Wins')
            s[0]+=1
            break
        elif (l[6]==l[3]==l[0]=='X') or (l[7]==l[4]==l[1]=='X') or (l[8]==l[5]==l[2]=='X') or (l[6]==l[7]==l[8]=='X') or (l[4]==l[3]==l[5]=='X') or (l[2]==l[1]==l[0]=='X') or (l[6]==l[2]==l[4]=='X') or (l[8]==l[4]==l[0]=='X') : 
            print('you win')
            s[1]+=1
            break
        elif lc.__len__()==0:
            print('Draw')
            break
    play=input('\nPress any key to play again or Press "n" to quit\n\n').strip().lower()
    if play=='no' or play =='n':
        break
