import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('График')
window.geometry('500x500')

x_label = tk.Label(text='X')
x_number = tk.Entry()

y_label = tk.Label(text='Y')
y_number = tk.Entry()

fun_label = tk.Label(text='Функция')
fun_number = tk.Entry()

def Grafic():
    fig, ax = plt.subplots()
    
    ax.set_title('График')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    x=np.linspace(int(x_number.get()), int(y_number.get()), 10)
    y=eval(fun_number.get())
    
    ax.plot(x, y)
    ax.grid()
    plt.show()
    

button = tk.Button(text='Построить', width=8, height=2, command=Grafic)

x_label.pack()
x_number.pack()

y_label.pack()
y_number.pack()

fun_label.pack()
fun_number.pack()

button.pack()
window.mainloop()