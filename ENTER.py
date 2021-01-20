from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import time
import quandl
import pandas as pd
import numpy as np
from sklearn import  model_selection
import math
from sklearn.tree import DecisionTreeClassifier

class Algo():
    def __init__(self, root):
        self.root=root
        
        self.label = Label(self.root, text='FLOWER PREDICTOR',bg='white', font=('arial', 30, 'bold'),fg='black')
        self.label.pack()

        self.t1=StringVar()
        self.t2=StringVar()
        self.t3=StringVar()
        self.t4=StringVar()
        self.t5=StringVar()

        self.label_1 = Label(root, text='Sepal Length :',bg='white', font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_1.place(x=30, y=180)

        self.T1 = Entry(root, textvariable=self.t1, bd=2)
        self.T1.place(x=250, y=180)

        self.label_2 = Label(root, text='Sepal Width :',bg='white', font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_2.place(x=30, y=250)

        self.T2 = Entry(root, textvariable=self.t2, bd=2)
        self.T2.place(x=250, y=250)
        
        self.label_3 = Label(root, text='Petal Length :',bg='white', font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_3.place(x=30, y=320)

        self.T3 = Entry(root, textvariable=self.t3, bd=2)
        self.T3.place(x=250, y=320)

        self.label_4 = Label(root, text='Petal Width :',bg='white', font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_4.place(x=30, y=390)

        self.T4 = Entry(root, textvariable=self.t4, bd=2)
        self.T4.place(x=250, y=390)


        ############################################################################################################################
        
        self.button1 = Button(root,  text='ENTER',relief='groove',bg="#ffffff", command=self.prediction, font=('arial', 12,'bold'))
        self.button1.place(x=150,y=620)

        self.button2 = Button(root,  text='RESET',relief='groove',bg="#ffffff", command=self.RESET, font=('arial', 12,'bold'))
        self.button2.place(x=350,y=620)

        self.button3 = Button(root,  text='BACK',relief='groove',bg="#ffffff", command=self.BACK, font=('arial', 12,'bold'))
        self.button3.place(x=550,y=620)

        self.T5 = Entry(root, textvariable=self.t5, bd=2,font=('arial', 14, 'bold'))
        self.T5.place(x=495, y=425)

        self.can=Canvas(root,bd=5,bg='white',width=200,height=200)
        self.can.place(x=500,y=190)

        ############################################################################################################################
        
        root.geometry('800x700+0+0')
        root.mainloop()

    def RESET(self):
        self.t1.set("")
        self.t2.set("")
        self.t3.set("")
        self.t4.set("")
        self.t5.set("")
        self.can.delete('all')
        

    def BACK(self):
        self.root.destroy()
        import main
        
    def prediction(self):
        if ( self.t1.get() == '' or self.t2.get() == '' or self.t3.get() == '' or self.t4.get() == ''):
            messagebox.showwarning("Incorrect", "Enter All Columns Values")
        else:
            self.predict()

    def predict(self):
        df=pd.read_csv('iris.csv')
        df.dropna(inplace=True)
        df.drop(['Id'],1,inplace=True)

        X = np.array(df.drop(['Species'],1))
        Y = np.array(df['Species'])

        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2)

        clf=DecisionTreeClassifier(max_depth=5)
        clf.fit(X_train, Y_train)
        accuracy = clf.score(X_test, Y_test)

        prediction1 = clf.predict([[int(self.t1.get()),int(self.t2.get()),int(self.t2.get()),int(self.t2.get())]])
        self.t5.set(prediction1)

        if prediction1=='Iris-setosa':
            self.img1=PhotoImage(file='saa.png')
            self.can.create_image(7,8,image=self.img1,anchor=NW)

        if prediction1=='Iris-virginica':
            self.img1=PhotoImage(file='caa.png')
            self.can.create_image(7,8,image=self.img1,anchor=NW)

        if prediction1=='Iris-versicolor':
            self.img1=PhotoImage(file='sii.png')
            self.can.create_image(7,8,image=self.img1,anchor=NW)
        


root = Tk()
root.title("PREDICTOR")
root.config(bg="honeydew2")
Can = Algo(root)
