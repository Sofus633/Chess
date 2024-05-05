from tkinter import *
from InputsManager import *
from Setting import *
import ShowManager


global window
global canva



def init():
    window.geometry("560x560")
    
    
    window.bind('<Button-1>', onclick, add='+')
    window.bind('<ButtonRelease-1>', onrealease, add='+')
    window.bind('<Motion>', onmotion, add='+')
    
    
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