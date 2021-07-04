import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import Entry, font, filedialog
from tkinter.constants import X, Y
from page import *
from algorithm import *

class Page2(Page):

    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)
        

        input = Label(self, text="Input", fg="blue", font= font.Font(size=8))
        input.place(x=10,y=5)

        label_1 = Label(self, text="IdM-Liste", font= font.Font(size=11))
        label_1.place(x=10,y=30)
        entry_1 = tk.Entry(self, bd=4)
        entry_1.place(x=200,y=30, width=170)
        entry_1.insert(0, "Datei")
        button_1 = tk.Button(self, text="Auswählen",command=lambda: self.select_file(entry_1,1), bd=4)
        button_1.place(x=380,y=27)

        label_2 = tk.Label(self, text="Benötigte Anwendungen", font= font.Font(size=11))
        label_2.place(x=10,y=80)
        entry_2 = tk.Entry(self, bd=4)
        entry_2.place(x=200,y=80, width=170)
        entry_2.insert(0, "Datei")
        button_2 = tk.Button(self, text="Auswählen",command=lambda: self.select_file(entry_2,2), bd=4)
        button_2.place(x=380,y=77)
        
        output = tk.Label(self, text="Output", fg="blue", font= font.Font(size=8))
        output.place(x=10,y=145)

        label_3 = tk.Label(self, text="Berechtigungsmatrix", font= font.Font(size=11))
        label_3.place(x=10,y=170)
        entry_3 = tk.Entry(self, bd=4)
        entry_3.place(x=200,y=170, width=170)
        entry_3.insert(0, "Ordner")
        button_3 = tk.Button(self, text="Auswählen",command=lambda: self.result_dest(entry_3,3), bd=4)
        button_3.place(x=380,y=167)

        label_4 = tk.Label(self, text="Übereinstimmungsliste", font= font.Font(size=11))
        label_4.place(x=10,y=220)
        entry_4 = tk.Entry(self, bd=4)
        entry_4.place(x=200,y=220, width=170)
        entry_4.insert(0, "Ordner")
        button_4 = tk.Button(self, text="Auswählen",command=lambda: self.result_dest(entry_4,4), bd=4)
        button_4.place(x=380,y=217)

        global precent
        precent = tk.StringVar()
        label_5 = tk.Label(self, text="Übereinstimmung", font= font.Font(size=11))
        label_5.place(x=10,y=270)
        entry_5 = tk.Entry(self, textvariable = precent, bd=4)
        entry_5.insert(0, "Übereinstimmung %")
        entry_5.place(x=200,y=270, width=170)
        
        
        

        start = tk.Button(self, text="Start", font= font.Font(size=13), command= self.run, bd=4)
        start.place(x=500,y=320, width=80, height=30)

    def select_file(self,x, index):
        x.delete(0,'end')
        file_path= filedialog.askopenfilename(title = "Select A File")
        x.insert(0,file_path)
        #check in which button
        if(index==1):
            global df_1
            df_1=functions.data_frame(file_path)
        if(index==2):
            global df_2
            df_2=functions.data_frame(file_path)

    def result_dest(self,x, index):
        global directory1,directory2
        x.delete(0,'end')
        if index ==3:
            directory1 = filedialog.asksaveasfilename(defaultextension='.xlsx')
            x.insert(0,directory1)
        if index ==4:
            directory2 = filedialog.asksaveasfilename(defaultextension='.xlsx')
            x.insert(0,directory2)

        
    def run(self):
        df_3 = functions.Berechtigungsmatrix(df_1,df_2)
        df_4 = functions.Ubereinstimmungsliste(df_1,df_2, precent.get())
        df_3.to_excel(directory1)
        df_4.to_excel(directory2)

        label_end = tk.Label(self, text="files saved", fg="green", font= font.Font(size=15))
        label_end.place(x=270,y=330)
