import tkinter as tk
from functools import partial
from tkinter import messagebox, ttk
from tkinter import *
root = tk.Tk()
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")
root.title("sheep")
def saludar(ventana):
    messagebox.showinfo(message="hello, thanks for saying that", title="soul")
    root.destroy()
text = Label(root, text="this is a sheep")
text.pack()
text2 = Label(root, text="his name is soul")
text2.pack()
image = PhotoImage(file="sheep.png")
img = Label(root, image=image)
img.pack()
text3 = Label(root, text="you should say hi to soul")
text3.pack()
boton = ttk.Button(text="hi", command=partial(saludar, root))
boton.place(x=100, y=200)
root.mainloop()
