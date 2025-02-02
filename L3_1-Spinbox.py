from tkinter import *

window: Tk = Tk(); window.title("L1_1-4_Buttons"); window.geometry("150x150"); window.config(background = "#ffffff")

frame = Frame(window)
frame.place(x = 5, y = 0)

Label(frame, text = "Listbox").pack()

scrollbar = Scrollbar(frame)

listbox: Listbox = Listbox(frame, height = 3)

scrollbar.config(command = listbox.yview)
scrollbar.pack(side = RIGHT, fill = Y)

listbox.pack()

inserts: list = ["1", "2", "3", "4", "5"]
for i in range(len(inserts)): listbox.insert(i, inserts[i])

def addItem(): listbox.insert(0, entry.get())

def deleteItem(): listbox.delete(END, END)

def resetList():
  listbox.delete(0, END)
  for i in range(len(inserts)): listbox.insert(i, inserts[i])

entry = Entry(frame)
entry.pack()

Button(frame, text = "Append item", command = addItem).pack()
Button(frame, text = "Delete item", command = deleteItem).pack()

menubar = Menu(window)

edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = edit)
edit.add_command(label = "Reset List", command = resetList)

window.config(menu = menubar)

window.mainloop()