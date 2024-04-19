from Setting import *
from PIL import Image,ImageTk
import time

def showboard():
    global canva
    global board
    for y in range(len(board)):
        for x in range(len(board[y])):
            if not board[y][x] == 0:
                image = Noir[board[y][x] if board[y][x] == 0 else board[y][x][0]] if board[y][x][1] else Blanc[board[y][x] if board[y][x] == 0 else board[y][x][0]]
                canva.create_image(x * 70+35,y * 70+35,image=image)
            
                
def showhand():
    global hand
    
    if hand[2] and hand[0] != 0:
        print(hand)
        canva.create_image(hand[3][0],hand[3][1],image=Noir[hand[0][0]] if hand[0][1] else Blanc[hand[0][0]])
    
    
def showboardpng():
    global boardimage
    canva.create_image(560//2,560//2,image=boardimage)