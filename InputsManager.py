from Setting import *
from Rules import *
import winsound
import threading
from pygame import *
from copy import deepcopy
import random

mixer.init()
mixer.music.load("Sounds\chessmusic" + ("2" if random.randint(0, 2) == 1 else "1") + ".mp3")
mixer.music.play()
mixer.music.set_volume(0.1)


def onclick(event):
    global board
    global hand
    global couleurtour
    global roi_danger
    x = event.x  // 70
    y = event.y  // 70
    print(board[y][x] ,  couleurtour)
    
    
    
    
    if 0 <= x  and x < 8 and 0 <= y and y < 8 and board[y][x][1] == couleurtour:
        print(event.y  // 70, event.x + 35 // 70)
        hand[0] = board[y][x]
        hand[1][0] = (x, y)
        board[y][x] = 0
        hand[2] = True
    
def onrealease(event):
    global board
    global hand
    global couleurtour
    x = event.x // 70
    y = event.y // 70
    if 0 <= x < 8 and 0 <= y < 8 and hand[2]:
        hand[1][1] = (x, y)
        hand[2] = False


        if IsLegal(hand, board):
            board_test = deepcopy(board)
            board_test[y][x] = hand[0]
            if roidanger(cara,board_test,hand[0][1]):
                print ("tout est bon")
                board[y][x] = hand[0]
                print(couleurtour)
                couleurtour = False if couleurtour == True else True
                print("SET TO",couleurtour)
                echemat()
            else:
                board[hand[1][0][1]][hand[1][0][0]] = hand[0]
        else:
            board[hand[1][0][1]][hand[1][0][0]] = hand[0]
        

        
def printboard(board):
    for y in range(len(board)):
        print('')
        for x in range(len(board[y])):
            print(board[y][x], end='' if board[y][x] != 0 else "          ")
    
def onmotion(event):
    global hand
    hand[3] = (event.x, event.y)
    
def musicbutton():
    global musicstate
    if musicstate == "Playing":
        mixer.music.pause()
        musicstate = 'Pause'
    else:
        mixer.music.play()
        musicstate = "Playing"