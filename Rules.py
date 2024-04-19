from Setting import *
from copy import deepcopy
pion = 1 
Tour = 2 
cavalier = 3
fou = 4 
roi = 5 
reine = 6 


def test(autorise,piece,posfin,posdep):
    print (posfin)
    print (posfin[0])
    if autorise[piece] == (abs(posfin[0] - posdep[0]) , abs(posfin[1] - posdep[1])) or autorise[piece] == (abs(posdep[0] - posfin[0]),abs (posdep[1] - posfin[1])):
        return True
    if autorise[piece] == (abs(posfin[1] - posdep[1]),abs(posfin[0] - posdep[0]) ) or autorise[piece] == (abs(posdep[1] - posfin[1]),abs(posdep[0] - posfin[0])):
        return True 
def testroie(autorise,piece,posfin,posdep):
    if test(autorise,piece,posfin,posdep) == True :
        return True 
    if autorise[piece] == (abs(posfin[0] - posdep[0])-1, abs(posfin[1] - posdep[1])) or autorise[piece] == (abs(posfin[1] - posdep[1]) +1,abs(posfin[0] - posdep[0]) ):
        return True

  

    

def testour(posfin,posdep,board):
    # Deplacement en y 
    if posdep[0] == posfin[0] and posdep[1] != posfin[1] :
        if posdep[1] < posfin[1] : 
            for i in range(posdep[1] , posfin[1]):
                if board[i][posdep[0]] != 0 :
                    return False
            return True 
        if posdep[1] > posfin[1] : 
            for i in range(posfin[1]+1,posdep[1]):
                if board[i][posdep[0]] != 0 :
                    return False
            return True 
 # Deplacement en x 
    if posdep[0] != posfin[0] and posdep[1] == posfin[1] :
        if posdep[0] < posfin[0] : 
            for i in range(posdep[0] , posfin[0]):
                if board[posdep[1]][i] != 0 :
                    return False
            return True 
        if posdep[0] > posfin[0] : 
            for i in range(posfin[0]+1,posdep[0]):
                if board[posdep[1]][i] != 0 :
                    return False
            return True 
    
    

def testfou(posfin,posdep,board) :
    # monter en y monte en x 
    if posdep[1] < posfin[1] and posdep[0] < posfin[0] :
       
        for i in range(1,abs(posdep[1] - posfin[1])) :
            print (i)
            if 0 <= posdep[1]+ i >= 8 or 0 <= posdep[0] + i >= 8 :
                return False
            if board[posdep[1]+ i][posdep[0] + i] != 0: 
                return False
        if abs(posfin[0]  - posdep[0])  == abs(posfin[1] - posdep[1]) :
            return True
    # desent en y monte en x 
    
    if posdep[1] > posfin[1] and posdep[0] < posfin[0] :
        for i in range(1,abs(posdep[1] - posfin[1])) :
            print (i)
            if 0 <= posdep[1]- i >= 8 or 0 <= posdep[0] + i >= 8 :
                return False
            if board[posdep[1] - i ][posdep[0]+ i] != 0: 
                return False
        if abs(posfin[0]  - posdep[0])  == abs(posfin[1] - posdep[1]) :
            return True
    #monte en Y desent en x
    if posdep[1] < posfin[1] and posdep[0] > posfin[0] :
        for i in range(1,abs(posdep[1] - posfin[1])) :
            print (i)
            if 0 <= posdep[1]+ i >= 8 or 0 <= posdep[0] - i >= 8 :
                return False
            if board[posdep[1] + i][posdep[0] -i] != 0: 
                return False
        if abs(posfin[0]  - posdep[0])  == abs(posfin[1] - posdep[1]) :
            return True
    # desent y desent x 
    if posdep[1] > posfin[1] and posdep[0] > posfin[0] :
        for i in range(1,abs(posdep[1] - posfin[1])) :
            print (i)
            if 0 <= posdep[1] - i >= 8 or 0 <= posdep[0] - i >= 8 :
                return False
            if board[posdep[1] - i][posdep[0] - i] != 0: 
                return False
        if abs(posfin[0]  - posdep[0])  == abs(posfin[1] - posdep[1]) :
            return True
                
def testpion(autorise,piece,posfin,posdep,board,hand) : 
    #blanc
    couleur = hand[0] if hand[0] == 0 else hand[0][1]
    if  couleur == True: 
        if autorise[piece] == (posdep[0] - posfin[0] ,posdep[1] - posfin[1]) and board[posfin[1]][posfin[0]] == 0:
                return True
        if posdep[1] == 6  :
            if autorise[piece] == (posdep[0] - posfin[0],posdep[1] - posfin[1] -1 ) and board[posfin[1]][posfin[0]] == 0 and board[posfin[1]+1][posfin[0]] == 0 :
                return True
        if board[posfin[1]][posfin[0]] != 0 :
            if (posdep[0]-1,posdep[1]-1) == posfin or (posdep[0]+1,posdep[1]-1) == posfin : 
                return True
       
    #noir
    if  couleur == False: 
        if autorise[piece] == ( posfin[0] - posdep[0] , posfin[1] - posdep[1]) and board[posfin[1]][posfin[0]] == 0:
            return True
        if posdep[1] == 1 :
            if autorise[piece] == ( posfin[0] - posdep[0] , posfin[1] - posdep[1]  -1 ) and board[posfin[1]][posfin[0]] == 0 and board[posfin[1]-1][posfin[0]] == 0 :
                return True
        if board[posfin[1]][posfin[0]] != 0 :
            if (posdep[0]+1, posdep[1]+1)== posfin or (posdep[0]-1, posdep[1]+1) == posfin : 
                return True
            

def IsLegal(hand,board):
    global autorise
    posdep = hand[1][0]
    posfin = hand[1][1]
    piece = hand[0] if hand[0] == 0 else hand[0][0]
    #pion
    if board[posfin[1]][posfin[0]] != 0 :
        if board[posfin[1]][posfin[0]][1] == hand[0][1] :
            return False
    
    if piece == pion :
        if testpion(autorise,piece,posfin,posdep,board,hand) :
            return True

    #Tour 
    if piece == Tour :
        if testour(posfin,posdep,board)  : 
            return True
    #cavalier 
    if piece == cavalier:
        if test(autorise,piece,posfin,posdep)  : 
            return True
    
    #fou 
    if piece == fou :
        if testfou(posfin,posdep,board)  :
            return True 

    #roi 
    if piece == roi :
        if testroie(autorise,piece,posfin,posdep)  :
            return True
    #reine 
    if piece == reine :
        if testfou(posfin,posdep,board)  : 
            return True 
        if testour(posfin,posdep,board)  :
            return True
    return False 
    
board_test = deepcopy(board)

cara = [(None, None), [(None, None), (None, None)]] 

def roidanger(cara,board,dernier_joueur): 
    global autorise
    global roi_danger
    global gagnen
     
    roi_danger = False
    for y in range(8):
        for x in range(8):
            print (board[y][x])
            if board[y][x]== (5, False) :
                poseroinoir = (x,y)
            if board[y][x] == (5, True) :
                poseroiblanc = (x,y)
    for y in range(8):
        print("a")
        for x in range(8):
            print("b")
            if board[y][x] != 0 :
                cara[0] = board[y][x]
                cara[1][0] = (x, y)
                if cara[0][1] == True: 
                    print(poseroinoir)
                    posfin = poseroinoir
                    couleur = board[posfin[1]][posfin[0]][1]
                else: 
                    posfin = poseroiblanc
                    couleur = board[posfin[1]][posfin[0]][1]
                print (cara)
                if cara[0][0] == 1 :
                    print ("1")
                    print(testpion(autorise,cara[0][0],posfin,cara[1][0],board,cara))
                    if testpion(autorise,cara[0][0],posfin,cara[1][0],board,cara) :
                        if dernier_joueur == couleur :
                            print ("tu ne peux pas mettre ton roie en danger")
                            return False
                        else :
                            print ("le roi est en danger")
                            roi_danger = True 
                if cara[0][0] == 2 :
                    print ("2")
                    print(testour(posfin,cara[1][0],board))
                    if testour(posfin,cara[1][0],board) : 
                        if dernier_joueur == couleur :
                            print ("tu ne peux pas mettre ton roie en danger")
                            return False
                        else :
                            print ("le roi est en danger")
                            roi_danger = True 
                if cara[0][0] == 3:
                    print ("3")
                    print(board[posfin[1]][posfin[0]][1])
                    if test(autorise,cara[0][0],posfin,cara[1][0]): 
                        if dernier_joueur == couleur :
                            print ("tu ne peux pas mettre ton roie en danger")
                            return False
                        else :
                            print ("le roi est en danger")
                            roi_danger = True 
                if cara[0][0] == 4 :
                    print ("4")
                    print(board[posfin[1]][posfin[0]][1])
                    if testfou(posfin,cara[1][0],board)  :
                        if dernier_joueur == couleur:
                            print ("tu ne peux pas mettre ton roie en danger")
                            return False
                        else :
                            print ("le roi est en danger")
                            roi_danger = True 
                if cara[0][0] == 6 :
                    print ("6")
                    if testfou(posfin,cara[1][0],board)  : 
                        if dernier_joueur == couleur :
                            print ("tu ne peux pas mettre ton roie en danger")
                            return False 
                        else :
                            print ("le roi est en danger")
                            roi_danger = True 
                    if testour(posfin,cara[1][0],board)  :
                        print ("tu ne peux pas mettre ton roie en danger")
                        if dernier_joueur == couleur:
                            return False
                        else :
                            print ("le roi est en danger")
                            roi_danger = True 
    return True 

def echemat():
    global gagnen
    posibilitenoir = []
    posibiliteblanc = []
    for y in range(8):
        for x in range(8):
            print (board[y][x])
            if board[y][x]== (5, False) :
                poseroinoir = (x,y)
                posibilitenoir.append((x,y)) 
            if board[y][x] == (5, True) :
                poseroiblanc = (x,y)
                posibiliteblanc.append((x,y)) 
    for y in range(8):
        for x in range(8):
            if board[y][x] != 0 : 
                if testroie(autorise,6,(x,y),poseroinoir) and board[y][x][1] != False : 
                    posibilitenoir.append((x,y)) 
                if testroie(autorise,6,(x,y),poseroiblanc) and board[y][x][1] != True :
                    posibiliteblanc.append((x,y)) 
            else:
                if testroie(autorise,6,(x,y),poseroinoir) : 
                    posibilitenoir.append((x,y)) 
                if testroie(autorise,6,(x,y),poseroiblanc):
                    posibiliteblanc.append((x,y)) 
    print ("efzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",posibiliteblanc)
    print ("efzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",posibilitenoir)
    for i in range(len(posibilitenoir)) :
        for y in range(8):
            print("a")
            for x in range(8):
                print("b")
                if board[y][x] != 0 :
                    cara[0] = board[y][x]
                    cara[1][0] = (x, y)
                    if cara[0][1] == True: 
                        print(posibilitenoir[i])
                        posfin = posibilitenoir[i]
                        print (cara)
                        if cara[0][0] == 1 :
                            print ("1")
                            if posibilitenoir[i] != True and testpion(autorise,cara[0][0],posfin,cara[1][0],board,cara) :
                                posibilitenoir[i] = True 
                        if cara[0][0] == 2 :
                            print ("2")
                            if posibilitenoir[i] != True and testour(posfin,cara[1][0],board) : 
                                posibilitenoir[i] = True 
                        if cara[0][0] == 3:
                            print ("3")
                            if posibilitenoir[i] != True and test(autorise,cara[0][0],posfin,cara[1][0]): 
                                posibilitenoir[i] = True 
                        if cara[0][0] == 4 :
                            print ("4")
                            
                            if posibilitenoir[i] != True and testfou(posfin,cara[1][0],board)  :
                                posibilitenoir[i] = True 
                            print ("6")
                            if posibilitenoir[i] != True and testfou(posfin,cara[1][0],board)  : 
                                posibilitenoir[i] = True 
                            if posibilitenoir[i] != True and testour(posfin,cara[1][0],board)  :
                                posibilitenoir[i] = True 
        num = 0
        print ("ooooooooooooooooooooooooooooooooooooooooooooooooooooooo",posibilitenoir)
    while True in posibilitenoir :
        num +=1 
        if posibilitenoir[num] == True :
            del posibilitenoir[num] 
        if num > len(posibilitenoir) :
            num = 0
    if len(posibilitenoir ) == 0 :
        gagnen = "Blanc" 
    if len(posibilitenoir ) == 0 :
        gagnen = Blanc 
    for i in range(len(posibiliteblanc)) :
        for y in range(8):
            print("a")
            for x in range(8):
                print("b")
                if board[y][x] != 0 :
                    cara[0] = board[y][x]
                    cara[1][0] = (x, y)
                    if cara[0][1] == False: 
                        print(posibiliteblanc[i])
                        posfin = posibiliteblanc[i]
                        print (cara)
                        if cara[0][0] == 1 :
                            print ("1")
                            if posibilitenoir[i] != True and testpion(autorise,cara[0][0],posfin,cara[1][0],board,cara) :
                                posibiliteblanc[i] = True   
                        if cara[0][0] == 2 :
                            print ("2")
                            if posibilitenoir[i] != True and testour(posfin,cara[1][0],board) : 
                                posibiliteblanc[i] = True   
                        if cara[0][0] == 3:
                            print ("3")
                        
                            if posibilitenoir[i] != True and test(autorise,cara[0][0],posfin,cara[1][0]): 
                                posibiliteblanc[i] = True  
                        if cara[0][0] == 4 :
                            print ("4")
                            if posibilitenoir[i] != True and testfou(posfin,cara[1][0],board)  :
                                posibiliteblanc[i] = True   
                            print ("6")
                            if posibilitenoir[i] != True and testfou(posfin,cara[1][0],board)  : 
                                posibiliteblanc[i] = True    
                            if posibilitenoir[i] != True and testour(posfin,cara[1][0],board)  :
                                posibiliteblanc[i] = True    
    num = 0
    print ("ooooooooooooooooooooooooooooooooooooooooooooooooooooooo",posibiliteblanc)
    while True in posibiliteblanc :
        num +=1 
        if posibiliteblanc[num] == True :
            del posibiliteblanc[num] 
        if num > len(posibiliteblanc) :
            num = 0
    if len(posibiliteblanc ) == 0 :
        gagnen = "Noir"