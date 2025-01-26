from tkinter import *

window: Tk = Tk(); window.title("L1_1-4_Buttons"); window.geometry("150x160"); window.config(background = "#ffffff")


frame = Frame(window)
frame.place(x = 5, y = 5)

Label(frame, text = "Listbox").pack()

scrollbar = Scrollbar(frame)

listbox: Listbox = Listbox(frame, height = 5)

scrollbar.config(command = listbox.yview)
scrollbar.pack(side = RIGHT, fill = Y)

listbox.pack()

inserts: list = ["H", "e", "l", "l", "o"]
for i in range(len(inserts)): listbox.insert(i, inserts[i])

def addItem(): listbox.insert(0, entry.get())

entry = Entry(frame)
entry.pack()

Button(frame, text = "Add item", command = addItem).pack()

window.mainloop()