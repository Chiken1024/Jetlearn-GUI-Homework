from tkinter import *
import tkinter.font as tkf


window: Tk = Tk()
window.title("L1_1-4_Buttons")
window.geometry("240x238")
window.config(background = "#33333f")

largeFont = tkf.Font(family = "Helvetica", size = 32, weight = "bold")
smallFont = tkf.Font(family = "Helvetica", size = 9, weight = "bold")


def open() -> None: pass

def delete() -> None: pass

def save() -> None: pass

def add() -> None: pass

functionNames: list = ["Open", "Delete", "Save", "Add"]
functions: list = [open, delete, save, add]


Label(window, text = "Memoriser", font = largeFont, background = "#66667f", foreground = "#ccccff").grid(row = 0, column = 0, padx = 5, pady = 5)

frame: Frame = Frame(window, background = "#4f4f5f")
frame.grid(row = 1, column = 0, padx = 5)

for i in range(4): Button(frame, text = functionNames[i], font = smallFont, background = "#66667f", foreground = "#ccccff", activebackground = "#ccccff", width = 8, command = functions[i]).grid(row = i // 3, column = i % 3 + (i // 3) * 2, padx = 5, pady = 5)

entry = Entry(frame, font = smallFont, background = "#66667f", foreground = "#ccccff", width = 20).grid(row = 1, column = 0, columnspan = 2, padx = 5)

listboxFrame = Frame(frame, background = "#ccccff")
listboxFrame.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)

listbox = Listbox(listboxFrame, background = "#66667f", foreground = "#ccccff", width = 33, height = 5)

listboxScrollbar = Scrollbar(listboxFrame, command = listbox.yview)
listboxScrollbar.pack(side = RIGHT, fill = Y)

listbox.pack()

window.mainloop()