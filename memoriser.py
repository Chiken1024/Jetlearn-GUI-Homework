from tkinter import *
import tkinter.font as tkf
from tkinter.filedialog import *


window: Tk = Tk()
window.title("Memoriser")
window.geometry("240x238")
window.config(background = "#33333f")

largeFont = tkf.Font(family = "Helvetica", size = 32, weight = "bold")
smallFont = tkf.Font(family = "Helvetica", size = 9, weight = "bold")


def open() -> None:
  fileIn = askopenfile(title = "Open File")

  if fileIn != None:
    listbox.delete(0, END)
    items = fileIn.readlines()

    for item in items: listbox.insert(END, item.strip())

def delete() -> None:
  selected: bool = False
  for i in range(len(listbox.get(0, END))):
    if listbox.selection_includes(i):
      selected = True
      break
  if selected: listbox.delete(listbox.curselection()[0])
  else: listbox.delete(0, END)

def save() -> None:
  fileOut = asksaveasfile(defaultextension = ".txt", filetypes = (("Text File", "*.txt"), ("Python File", "*.py")))

  if fileOut != None:
    for item in listbox.get(0, END): print(item.strip(), file = fileOut)

def add() -> None:
  selected: bool = False
  for i in range(len(listbox.get(0, END))):
    if listbox.selection_includes(i):
      selected = True
      break
  if selected:
    
    listbox.insert(listbox.curselection()[0], entry.get())
    listbox.delete(listbox.curselection()[0])
  else: listbox.insert(END, entry.get())
  entry.delete(0, END)


functionNames: list = ["Open", "Delete", "Save", "Add"]
functions: list = [open, delete, save, add]


Label(window, text = "Memoriser", font = largeFont, background = "#66667f", foreground = "#ccccff").grid(row = 0, column = 0, padx = 5, pady = 5)

frame: Frame = Frame(window, background = "#4f4f5f")
frame.grid(row = 1, column = 0, padx = 5)

for i in range(4): Button(frame, text = functionNames[i], font = smallFont, background = "#66667f", foreground = "#ccccff", activebackground = "#ccccff", width = 8, command = functions[i]).grid(row = i // 3, column = i % 3 + (i // 3) * 2, padx = 5, pady = 5)

entry: Entry = Entry(frame, font = smallFont, background = "#66667f", foreground = "#ccccff", width = 20)
entry.grid(row = 1, column = 0, columnspan = 2, padx = 5)

listboxFrame: Frame = Frame(frame, background = "#ccccff")
listboxFrame.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)

listbox: Listbox = Listbox(listboxFrame, background = "#66667f", foreground = "#ccccff", width = 33, height = 5)

listboxScrollbar: Scrollbar = Scrollbar(listboxFrame, command = listbox.yview)
listboxScrollbar.pack(side = RIGHT, fill = Y)

listbox.pack()


window.mainloop()