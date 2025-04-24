from tkinter import*
from matplotlib import pyplot as plt
import tkinter
main=tkinter.Tk()
main.title("Phases of machine learning algorithm")
main.geometry("1200x600")
main.config(bg="pink")

def dsc():
 name="this is the dataset collection phase"
 text.delete('1.0',END)
 text.insert(END,"\n")
 text.insert(END,name)

def dspp():
 name = "this is the dataset preprocessing phase"
 text.delete('1.0', END)
 text.insert(END, "\n")
 text.insert(END, name)



def cas():
 algm = ["SVM", "RF", "KNN"]
 accuracy = [85.2, 78.5, 92.1]
 text.delete('1.0', END)
 text.insert(END, "\n")
 plt.bar(algm, accuracy, color="blue")
 plt.xlabel("Algorithms")
 plt.ylabel("Accuracy")
 plt.title("Algorithm Accuracy Comparison")
 plt.show()


font=('arial',14,'bold')
title=Label(main,text="Machine learning algm in the form of buttons")
title.config(bg='purple',fg='orange',font=font,height=3,width=100)
title.place(x=0,y=0)

font1=('times',12,'bold')
dsc=Button(main,text="Dataset Collection",command=dsc)
dsc.config(font=font1,bg='blue',fg='white')
dsc.place(x=50, y=90)


dspp=Button(main,text="Dataset Preprocessing",command=dspp)
dspp.config(font=font1,bg='blue',fg='white')
dspp.place(x=180, y=90)

cas=Button(main,text="Calc accuracy score",command=cas)
cas.config(font=font1,bg='blue',fg='white')
cas.place(x=320, y=90)

text=Text(main,height=25,width=90)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=50,y=130)
text.config(font=font)
main.mainloop()

