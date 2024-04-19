from PIL import Image,ImageTk
from tkinter import *
global hand
global board
global nombredecoup
global window
global canva
global style
global boardimage
global couleurtour
global roi_danger
global gagnen
global musicstate


musicstate = "Playing"
style = '1'
nombredetour = 0
couleurtour = True
roi_danger = False
window = Tk()
canva = canva = Canvas(window , width=560, height=560, bg='ivory')
boardimage = PhotoImage(file="PngOther\Board.png")
#     Piece   couleur    Posdeb     PosFin     clicked   handposition
hand = [(None, None), [(None, None), (None, None)], False, (None, None)]
gagnen = None

board = [
        [(2, False), (3, False), (4, False), (5, False), (6, False), (4, False), (3, False), (2, False)],
        [(1, False), (1, False), (1, False), (1, False), (1, False), (1, False), (1, False), (1, False)],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [(1, True), (1, True), (1, True), (1, True), (1, True), (1, True), (1, True), (1, True)],
        [(2, True), (3, True), (4, True), (6, True), (5, True), (4, True), (3, True), (2, True)],
    ]

autorise = {
    0 : (0,1),
    1 : (0,1),
    2 : (0,1),
    3 : (2,1),
    4 : (-1,1),
    5 : (0,1),
    6 : (0,1)
    }

Blanc = {
    0 : None,
    1 : PhotoImage(file="Png" + style + "/pion0.png"),
    2 : PhotoImage(file="Png" + style + "/Tour0.png"),
    3 : PhotoImage(file="Png" + style + "/Cavalier0.png"),
    4 : PhotoImage(file="Png" + style + "/Fou0.png"),
    5 : PhotoImage(file="Png" + style + "/Roi0.png"),
    6 : PhotoImage(file="Png" + style + "/Reinne0.png")
}

Noir = {
    0 : None,
    1 : PhotoImage(file="Png" + style + "/pion1.png"),
    2 : PhotoImage(file="Png" + style + "/Tour1.png"),
    3 : PhotoImage(file="Png" + style + "/Cavalier1.png"),
    4 : PhotoImage(file="Png" + style + "/Fou1.png"),
    5 : PhotoImage(file="Png" + style + "/Roi1.png"),
    6 : PhotoImage(file="Png" + style + "/Reinne1.png")
}

def win(winner):
    text = Label(window, text = winner + " a gagner")