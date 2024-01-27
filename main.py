import tkinter as tk
from functools import partial
from tkinter import messagebox, ttk
from tkinter import *
root = tk.Tk()
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")
root.title("sheep")
def saludar(ventana):
    messagebox.showinfo(message="hola, gracias por decir eso", title="soul")
    root.destroy()
text = Label(root, text="la imagen de abajo es una oveja")
text.pack()
text2 = Label(root, text="su nombre es soul")
text2.pack()
image = PhotoImage(file="sheep.png")
img = Label(root, image=image)
img.pack()
text3 = Label(root, text="deberias de saludarla")
text3.pack()
boton = ttk.Button(text="saludar", command=partial(saludar, root))
boton.place(x=100, y=200)
root.mainloop()
