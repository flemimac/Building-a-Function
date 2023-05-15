# EN | Building a Function
Building a function. Enter the value of the X and Y range to build a function in this limit. 
The program is written in Python version 3.10.5.
Libraries used:
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Numpy](https://numpy.org/doc/)
- [Matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)

# How the code works?
Install the necessary libraries and give them short names.
```python
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
```

In the first three lines, we create a window, assign it a name and dimensions.
In the following lines we create a text and an input field
```python
window = tk.Tk()
window.title('График')
window.geometry('500x500')

x_label = tk.Label(text='X')
x_number = tk.Entry()

y_label = tk.Label(text='Y')
y_number = tk.Entry()

fun_label = tk.Label(text='Функция')
fun_number = tk.Entry()
```

The heart of the code. 
Created two variables with the value plt.subplots(). Creating the name of the graph, the line X and Y.

- The variable X was assigned the value np.linspace with the values that the user entered.
- The variable Y was assigned the value eval, which analyzes the formula for constructing the function.

At the end we output the values.
```python
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
```
We create a button that, when activated, turns on the "Graphics" function and displays all the buttons/text at the end of the code.
```python
button = tk.Button(text='Построить', width=8, height=2, command=Grafic)

x_label.pack()
x_number.pack()

y_label.pack()
y_number.pack()

fun_label.pack()
fun_number.pack()

button.pack()
window.mainloop()
```

## An example of how the program works:

![image](https://user-images.githubusercontent.com/64695348/232309517-29a65960-e996-4cd2-b5c8-893225510e98.png)

Formula Examples:
- Parabola formula - x**2
- Hyperbola formula - k/x (k - any value)

Mathematical signs:
- Addition - "+"
- Subtraction - "-"
- Division - "/"
- Multiplication - "*"
- Second degree - "**k" (k - any value)





# RU | Построение функции
Построение функции. Введите значение диапазона X и Y, чтобы построить функцию в этом пределе.
Программа написана на Python версии 3.10.5.
Используемые библиотеки:
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Numpy](https://numpy.org/doc/)
- [Matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)

# Как работает код?
Устанавливаем необходимые библиотеки и даем им короткие имена.

```python
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
```

В первых трех строках мы создаем окно, присваиваем ему название и размеры.
В следующих строках мы создаем текст и поле ввода.
```python
window = tk.Tk()
window.title('График')
window.geometry('500x500')

x_label = tk.Label(text='X')
x_number = tk.Entry()

y_label = tk.Label(text='Y')
y_number = tk.Entry()

fun_label = tk.Label(text='Функция')
fun_number = tk.Entry()
```

Сердце кода.
Создал две переменные со значением plt.subplots(). Создаем название графика, линии X и Y.

- Переменной X было присвоено значение np.linspace со значениями, которые ввел пользователь.
- Переменной Y было присвоено значение eval, которое анализирует формулу для построения функции.

В конце мы выводим значения.
```python
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
```
Мы создаем кнопку, которая при активации включает функцию "Графика" и отображаем все кнопки/текст в конце кода.
```python
button = tk.Button(text='Построить', width=8, height=2, command=Grafic)

x_label.pack()
x_number.pack()

y_label.pack()
y_number.pack()

fun_label.pack()
fun_number.pack()

button.pack()
window.mainloop()
```

## Пример того, как работает программа:

![image](https://user-images.githubusercontent.com/64695348/232309521-7f67a6bf-02b9-4ca7-a7fa-bad6142e3091.png)

Примеры формул:
- Формула параболы - x**2
- Формула гиперболы - k/x (k - любое значение)

Математические знаки:
- Дополнение - "+"
- Вычитание - "-"
- Разделение - "/"
- Умножение - "*"
- Степень числа - "**k" (k - любое значение)
