import tkinter as tk
from tkinter import *
from page import *
from tkinter import Entry, font, filedialog
from tkinter.constants import X, Y
import pandas as pd
from algorithm import *

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        

        lbli= tk.Label(self, text='Input', fg="blue", font= font.Font(size=8))
        lbli.place(x=10, y=5)

        
        lblo= tk.Label(self, text='Output', fg="blue", font= font.Font(size=8))
        lblo.place(x=10, y=245)

        lbl1= tk.Label(self, text='IDM-Liste', font= font.Font(size=11))
        lbl1.place(x=10, y=30)
        e1= tk.Entry(self, bd=4)
        e1.insert (0, "Datei" )
        e1.place(x=200, y=30, width=170)
        b1= tk.Button(self, text ='Auswählen', command =lambda: self.select_file(e1,1), bd=4)
        b1.place(x=380, y=27)

        lbl2= tk.Label(self, text='Benötigte Anwendungen', font= font.Font(size=11))
        lbl2.place(x=10, y=80)
        e2= tk.Entry(self, bd=4)
        e2.insert (0, "Datei" )
        e2.place(x=200, y=80, width=170)
        b2= tk.Button(self, text ='Auswählen', command =lambda: self.select_file(e2,2), bd=4)
        b2.place(x=380, y=77)

        
        lbl3= tk.Label(self, text='Cluster-Liste', font= font.Font(size=11))
        lbl3.place(x=10, y=130)
        e3= tk.Entry(self, bd=4)
        e3.insert (0, "Datei" )
        e3.place(x=200, y=130, width=170)
        b3= tk.Button(self, text ='Auswählen', command =lambda: self.select_file(e3,3), bd = 4)
        b3.place(x=380, y=127)

        
        lbl4= tk.Label(self, text='BRC-Template', font= font.Font(size=11)) 
        lbl4.place(x=10, y=180)
        e4= tk.Entry(self, bd=4)
        e4.insert (0, "Datei" )
        e4.place(x=200, y=180, width=170)
        b4= tk.Button(self, text ='Auswählen', command =lambda: self.select_file(e4,4), bd=4)
        b4.place(x=380, y=177)

        lbl5= tk.Label(self, text='BRC Template', font= font.Font(size=11))
        lbl5.place(x=10, y=270)
        e5= tk.Entry(self, bd=4)
        e5.insert (0, "Ordner" )
        e5.place(x=200, y=270, width=170)
        b5= tk.Button(self, text ='Auswählen', command =lambda: self.result_dest(e5), bd=4)
        b5.place(x=380, y=267)

        b6= tk.Button(self, text='Start', font= font.Font(size=13), command= self.run, bd=4)
        b6.place(x=500,y=320, width=80, height=30)

    def select_file(self, x, index):
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
        if(index==3):
            global df_3
            df_3=functions.data_frame(file_path)
        if(index==4):
            global df_4
            df_4=functions.data_frame(file_path)

    def result_dest(self,x):
        global directory
        x.delete(0,'end')
        directory = filedialog.asksaveasfilename(defaultextension='.xlsx')
        x.insert(0,directory)

    def run(self):
            df_5= functions.BRC_Template(df_1,df_2,df_3,df_4)
            df_5.to_excel(directory)

            label_end = tk.Label(self, text="files saved", fg="green", font= font.Font(size=15))
            label_end.place(x=270,y=330)

            













