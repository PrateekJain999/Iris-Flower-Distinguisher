from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time

class IRIS():
    def __init__(self, root):
        self.root=root
        self.root.geometry('800x600')

        self.l1 = Label(self.root, text='FLOWER PREDICTOR',bg='grey88', font=('arial', 30, 'bold'),bd=3)
        self.l1.pack()

        self.i1=PhotoImage(file='iris.png')
        self.l2=Label(self.root,image=self.i1)
        self.l2.place(x=50,y=100)


        self.b1 = Button(self.root, width=10, text='ENTER',bg='grey91',command=self.E1,font=('arial', 10, 'bold'),relief='groove')
        self.b1.place(x=60,y=400)

        self.b2 = Button(self.root, width=10, text='EXPLAIN',bg='grey91',command=self.E3,font=('arial', 10, 'bold'),relief='groove')
        self.b2.place(x=260,y=400)

        self.b3 = Button(self.root, width=10, text='EXIT',bg='grey91',command=self.EXIT,font=('arial', 10, 'bold'),relief='groove')
        self.b3.place(x=660,y=400)

        self.b4 = Button(self.root, width=10, text='ABOUT',bg='grey91',command=self.E2,font=('arial', 10, 'bold'),relief='groove')
        self.b4.place(x=460,y=400)

    def E1(self):
        self.p=Progressbar(self.root,length=200,orient=HORIZONTAL,value=0,mode='determinate')
        self.p.place(x=300,y=500)
        self.p['maximum']=50000
        self.ma=0
        
        self.I1()
        
    def I1(self):
        self.ma+=500
        self.p['value']=self.ma
        if self.p['value']<50000:
            self.root.after(100,self.I1)
        elif self.p['value']==50000:
            self.root.destroy()
            import ENTER

    def E2(self):
        self.p=Progressbar(self.root,length=200,orient=HORIZONTAL,value=0,mode='determinate')
        self.p.place(x=300,y=500)
        self.p['maximum']=50000
        self.ma=0
        
        self.I2()
        
    def I2(self):
        self.ma+=500
        self.p['value']=self.ma
        if self.p['value']<50000:
            self.root.after(100,self.I2)
        elif self.p['value']==50000:
            self.root.destroy()
            import ABOUT

    def E3(self):
        self.p=Progressbar(self.root,length=200,orient=HORIZONTAL,value=0,mode='determinate')
        self.p.place(x=300,y=500)
        self.p['maximum']=50000
        self.ma=0
        
        self.I3()
        
    def I3(self):
        self.ma+=500
        self.p['value']=self.ma
        if self.p['value']<50000:
            self.root.after(100,self.I3)
        elif self.p['value']==50000:
            self.root.destroy()
            import EXPLAIN

    def EXIT(self):
        a=messagebox.askquestion("EXIT", "Do You Want To Exit.")

        if a=='yes':
             self.root.destroy()
        elif a=='No':
            pass

root = Tk()
root.title("FLOWER PREDICTOR")
root.config(bg="honeydew2")
Can = IRIS(root)
