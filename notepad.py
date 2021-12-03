from tkinter.filedialog import *
import tkinter as tk

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Notepad")
canvas.config(bg="#CCFFFF")
top = Frame(canvas)
top.pack(padx=10, pady=5, anchor='nw')
b1 = Button(canvas, text="Open", bg="white")
b1.pack(in_=top, side=LEFT)

b2 = Button(canvas, text="Save", bg="white")
b2.pack(in_=top, side=LEFT)

b3 = Button(canvas, text="Clear", bg="white")
b3.pack(in_=top, side=LEFT)

b4 = Button(canvas, text="Exit", bg="white")
b4.pack(in_=top, side=LEFT)

entry = Text(canvas, bg="#FFFFCC", font =("poppins", 15))
entry.pack(padx=5, pady=5, expand=TRUE, fill=BOTH)

canvas.mainloop()
