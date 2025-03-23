from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox as tkmsg


window: Tk = Tk()
window.title("Multiplication Table Generator")
window.geometry("365x165")
window.config(background = "#222222")

largeFont = tkfont.Font(family = "Helvetica", size = 18, weight = "bold")
smallFont = tkfont.Font(family = "Helvetica", size = 12, weight = "bold")


class MultiplicationTable:
  def __init__(self, number: int, length: int) -> None:
    self.number: int = number
    self.length: int = length
  
  def generate(self) -> list[int]:
    numberList: list[int] = []
    for i in range(self.length): numberList.append(self.number * (i + 1))
    return numberList


def generate() -> None:
  if int(numberSpinbox.get()) != 0 and int(lengthSpinbox.get()) != 0:
    multiplicationTableWindow: Tk = Tk()
    multiplicationTableWindow.title("Multiplication Table")
    multiplicationTableWindow.geometry("365x365")
    multiplicationTableWindow.config(background = "#222222")

    tableFrame: Frame = Frame(multiplicationTableWindow, background = "#888888")
    tableFrame.grid(row = 0, column = 0, padx = 5, pady = 5)

    multiplicationTable: MultiplicationTable = MultiplicationTable(numberSpinbox.get(), lengthSpinbox.get())
  else: tkmsg.showinfo("Insufficient data!", "You haven't entered a valid number into one or both of the boxes! Please do so before generating.")


Label(window, text = "Multiplication Table Generator", font = largeFont, background = "#bbbbbb").grid(row = 0, column = 0, padx = 5, pady = 5)

frame: Frame = Frame(window, background = "#888888")
frame.grid(row = 1, column = 0)

Label(frame, text = "Enter your number:", font = smallFont, width = 15, background = "#bbbbbb").grid(row = 0, column = 0, padx = 5, pady = 5)

numberSpinbox: Spinbox = Spinbox(frame, from_ = 0, to = 8, font = smallFont, width = 9, background = "#bbbbbb")
numberSpinbox.grid(row = 0, column = 1, padx = 5, pady = 5)

Label(frame, text = "Select the length:", font = smallFont, width = 15, background = "#bbbbbb").grid(row = 1, column = 0, padx = 5, pady = 5)

lengthSpinbox: Spinbox = Spinbox(frame, from_ = 0, to = 8, font = smallFont, width = 9, background = "#bbbbbb")
lengthSpinbox.grid(row = 1, column = 1, padx = 5, pady = 5)

Button(frame, text = "Generate Table", font = smallFont, width = 20, background = "#bbbbbb", command = generate).grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)


window.mainloop()