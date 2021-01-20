from tkinter import *
import pandas as pd
import numpy as np

class Algo():
    def __init__(self, root):
        self.root=root
        self.root.geometry('900x600')

        self.i1=PhotoImage(file='img.png')
        self.l2=Label(self.root,image=self.i1)
        self.l2.place(x=30,y=30)

        self.l1=Label(self.root,text="FLOWER PREDICTOR",bg='white',font=('arial', 20, 'bold'))
        self.l1.place(x=480,y=50)

        self.l2=Label(self.root,text="Version : 1.0",bg='white',font=('arial', 10, 'bold'))
        self.l2.place(x=570,y=130)

        self.l3=Label(self.root,text="CopyRight @2019",bg='white',font=('arial', 15, 'bold'))
        self.l3.place(x=550,y=330)

        self.l4=Label(self.root,text="Contact No : 9997481571",bg='white',font=('arial', 15, 'bold'))
        self.l4.place(x=550,y=380)

        self.l5=Label(self.root,text="Gmail : jain22719@gmail.com",bg='white',font=('arial', 15, 'bold'))
        self.l5.place(x=550,y=430)

        self.b1 = Button(self.root, width=10, text='BACK',bg='white',font=('arial', 10, 'bold'),command=self.call)
        self.b1.place(x=750,y=530)

    def call(self):
        self.root.destroy()
        import main
        

root = Tk()
root.title("ABOUT")
root.config(bg="honeydew2")
Can = Algo(root)
