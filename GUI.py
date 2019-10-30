from tkinter import *
import tkinter as tk
from algorithm import  *
import tkinter.scrolledtext as scrolledtext


def submit():
  output.delete('1.0',END)
  input1 = textbox.get("1.0",END)
  x = scanner(input1)
  #x = open("output.txt", "r")
  output.insert(INSERT, x)

def clear():
    textbox.delete('1.0',END)
    output.delete('1.0',END)

def ex_fn():
    window.destroy()

def restart():
    output.delete('1.0',END)
    #textbox.delete('1.0',END)

window = Tk()

window.title('TINY Scanner')
window.configure(background='dodgerblue')
window.geometry('500x500+450+100')

Label(window, text='TINY code', fg='black', bg='white', font=('comicsans', 14)).place(x=20,y=2)

textbox = scrolledtext.ScrolledText(master = window,undo=True,height=40)
textbox.place(x=20,y=30)

Button(command = submit ,text ="Submit",bg='springgreen').place(x=615,y=675)
Button(command = clear ,text ="Clear",bg='gray64').place(x=574,y=675)


Label(window, text='Output', fg='black', bg='white', font=('comicsans', 14)).place(x=700,y=2)

output = scrolledtext.ScrolledText(master = window,undo=True,height=40)
output.place(x=700,y=30)

Button(command = restart ,text ="Restart",bg='yellow2').place(x=1260,y=675)
Button(command = ex_fn ,text ="EXIT",bg='red2').place(x=1310,y=675)

window.mainloop()
