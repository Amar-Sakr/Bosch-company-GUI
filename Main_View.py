import tkinter as tk
from tkinter import filedialog
from page import *
from page1 import *
from page2 import *
from page3 import *


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        global b1,b2,b3
        b1 = tk.Button(buttonframe, text="Anleitung", command=lambda:[p1.lift(),self.button_click(1)])
        b2 = tk.Button(buttonframe, text="Schritt 1", command=lambda:[p2.lift(),self.button_click(2)])
        b3 = tk.Button(buttonframe, text="Schritt 2", command=lambda:[p3.lift(),self.button_click(3)])

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()
    
    def button_click(self,x):
        global b1,b2,b3
        if(x==1):
            b1.configure(bg="#2079bb")
            b2.configure(bg="SystemButtonFace")
            b3.configure(bg="SystemButtonFace")
        if(x==2):
            b2.configure(bg="#2079bb")
            b1.configure(bg="SystemButtonFace")
            b3.configure(bg="SystemButtonFace")
        if(x==3):
            b3.configure(bg="#2079bb")
            b1.configure(bg="SystemButtonFace")
            b2.configure(bg="SystemButtonFace")


if __name__ == "__main__":
    root = tk.Tk()
    #root.iconbitmap(r'C:\Users\AYM1BH\Desktop\GUI\bosch.png')
    root.tk.call('wm','iconphoto',root._w,tk.PhotoImage(file=r'C:\Users\AYM1BH\Desktop\GUI\bosch.png'))
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x400")
    root.title("Bosch")
    root.mainloop()
