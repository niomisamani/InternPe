#Python project of TIC-TAC-TOE GAME
	
def CheckWin(grid):
    for i in range(3):
        if grid[i][0]==grid[i][1] and grid[i][1]==grid[i][2]:
            return 1
        if grid[0][i]==grid[1][i] and grid[1][i]==grid[2][i]:
            return 1
    if grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2]:
        return 1
    elif (grid[0][2]==grid[1][1] and grid[1][1]==grid[2][0]):
        return 1
    else:
        return 0

def Board(grid):
   print("-------------")
   for i in range(3):
        print("|   |   |   |")
        for j in range(3):
           print("| ",grid[i][j],sep=" ",end="")

        print("|\n|   |   |   |")
        print("-------------")
opt1='X'
opt2='X'           
i=1
player=1
res=0
response=""
grid=[['1','2','3'],['4','5','6'],['7','8','9']]
p1=input("Enter Player1 Name: ")
p2=input("Enter Player2 Name: ")
ch=input("Press any key to toss......")
import random
randnum=random.randrange(1,10)
if(randnum<=5):
    print("Player1 wins the toss")
    player=1
else:
    print("Player2 wins the toss")
    player=2
while True:
    print("Player ",player)
    ch=input("Enter your choice 'X' or 'O' : ")
    if ch=='X' or ch=='O':
        break
if player==1 and ch=='O':
        opt1=ch
elif(player==1 and ch=='X'):
        opt2='O'
elif(player==2 and ch=='O'):
        opt2=ch
else:
        opt1='O'
print("\nPlayer 1 (",opt1,"), Player 2 (",opt2,")")
while(i<=9 and response!='Q'):
    Board(grid)
    print("\nPress 1-9 for Square 1 to 9, Press Q to Quit")
    print("Player " ,player," : ")
    response=input("Enter your choice:")
    if player==1:
        mark=opt1
    else:
        mark=opt2
    if(response=='1' and grid[0][0]=='1'):
        grid[0][0]=mark
    elif(response=='2' and grid[0][1]=='2'):
        grid[0][1]=mark
    elif(response=='3' and grid[0][2]=='3'):
        grid[0][2]=mark
    elif(response=='4' and grid[1][0]=='4'):
        grid[1][0]=mark
    elif(response=='5' and grid[1][1]=='5'):
        grid[1][1]=mark
    elif(response=='6' and grid[1][2]=='6'):
        grid[1][2]=mark
    elif response=='7' and grid[2][0]=='7':
        grid[2][0]=mark
    elif(response=='8' and grid[2][1]=='8'):
        grid[2][1]=mark
    elif(response=='9' and grid[2][2]=='9'):
        grid[2][2]=mark
    else:
        if (response!='Q'):
            print("Wrong input!!!")
        continue
    res=CheckWin(grid)
    if(res==1):
        break
    i+=1
    if player==1:
        player=2
    else:
        player=1

Board(grid)
if (i>9):
    print("Game is draw")
elif (res==1):
    print("Congratulations!!! Player ",player,", You win....")
else:
    if player==1:
        player=2
    else:
        player=1
    print("Player ",player," You Quit!!! Thanks for playing the game.....")
