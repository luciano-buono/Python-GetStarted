def clc(): print ("\n" * 40)

move1= None
a= ['1', '2', '3']

def verif(move):
    while( not (move in a)   ):
        print("your move is invalid\n")
        move= input("choose your move\n")

def checkwin(move1,move2):
    if(move1 ==  move2):
        print("Draw")

    if(move1 == '1' and move2 == '2'):
        print("Player 2 wins")

    if(move1 == '2' and move2 == '1'):
        print("Player 1 wins")



move1= input("Player1, Choose:\n 1 for rock \n 2 for paper \n 3 for scissors\n")
verif(move1)
 
move2= input("Player2, Choose:\n 1 for rock \n 2 for paper \n 3 for scissors\n")
verif(move2)

checkwin(move1,move2)


