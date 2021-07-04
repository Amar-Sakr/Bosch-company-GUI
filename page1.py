import tkinter as tk
from page import *

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Read the following instructions")
       label.pack(side="top", fill="both", expand=True)

       txt = "Schritt 1: \n \n1.Auszug aus IdM2.0 für Fachabteilung auswählen \n2.Tabelle mit den benötigten Anwendungen und IT-Rollen auswählen \n3.Output: Berechtigungsmatrix und Liste mit hoher Übereinstimmung \n \nSchritt 2: \n \n1.Auszug aus IdM2.0 für Fachabteilung auswählen \n2.Tabelle mit den benötigten Anwendungen und IT-Rollen auswählen \n3.Ausgefüllte Liste mit Clustern (Business Roles) von der Fachabteilung \n4.BRC-Template (idealerweise bereits mit ausgefüllter Role Definition) \n5.Output: BRC-Template mit ausgefülltem Role Content"
       text= tk.Text(self)
       text.insert("1.0",txt)
       text.pack()
