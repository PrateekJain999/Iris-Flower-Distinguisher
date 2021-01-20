from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import time
import quandl
import pandas as pd
import numpy as np
from sklearn import  model_selection
import math

class Algo():
    def __init__(self, root):
        self.root=root
        self.root.geometry('900x730')

        self.df=pd.read_csv('iris.csv')
        
        self.T1 = Text(self.root,bd=5,width=80,height=8)
        self.T1.place(x=125, y=50)
        self.T1.insert(END,self.df.head())

        self.i1=PhotoImage(file='iris.png')
        self.l2=Label(self.root,image=self.i1)
        self.l2.place(x=100,y=210)
        
        a="The Iris flower data is a multivariate data set introduced by the British statistician and biologist \nRonald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example \nof linear discriminant analysis . It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.\n\n\n1. There are 150 observations with 4 features each (sepal length, sepal width, petal,length, petal \n   width).\n2. There are no null values, so we don't have to worry about that.\n3. There are 50 observations of each species (setosa, versicolor, virginica).\n\nFor More Info : https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342"

        self.T2 = Text(self.root,bd=5,width=102,height=12)
        self.T2.place(x=36, y=485)
        self.T2.insert(END,a)

        self.b1 = Button(self.root, width=10, text='BACK',bg='white',font=('arial', 10, 'bold'),command=self.call)
        self.b1.place(x=800,y=695)

    def call(self):
        self.root.destroy()
        import main
        
        

root = Tk()
root.title("EXPLAIN")
root.config(bg="honeydew2")
Can = Algo(root)
