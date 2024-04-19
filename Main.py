from tkinter import *
from InputsManager import *
from Setting import *
import ShowManager


global window
global canva



def init():
    window.geometry("660x560")
    
    button = Button(window, text="Music", command=musicbutton)
    
    window.bind('<Button-1>', onclick, add='+')
    window.bind('<ButtonRelease-1>', onrealease, add='+')
    window.bind('<Motion>', onmotion, add='+')
    
    
    button.place(x = 600, y= 50)
    window.after(100, main)
    return window, canva

def main():
    canva.delete('all')
    canva.pack(side=LEFT)
    if gagnen == None:
        ShowManager.showboardpng()
        ShowManager.showboard()
        ShowManager.showhand()
    else:
        win(gagnen) 
        

    window.after(100, main)
    
    
window, canva = init()
window.mainloop()