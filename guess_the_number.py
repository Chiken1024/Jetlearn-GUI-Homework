from tkinter import *
import tkinter.messagebox
from random import randint


window = Tk(); window.title("L1_1-4_Buttons"); window.geometry("308x194"); window.config(background = "#cccccc")


numberRange = [0, 20]
number = None

name = None


def confirmName():
  if enterName.get() != "":
    global numberRange, number, name

    name = enterName.get()
  
    if number == None: number = randint(numberRange[0], numberRange[1])
  else:
    tkinter.messagebox.showinfo("No name!", "Please enter a name to confirm.")

def confirmChoice():
  global name
  
  if enterNumber.get() != "":
    if name != None:
      global numberRange, number
      
      guess = int(enterNumber.get())
      if guess < numberRange[0] or guess > numberRange[1]: tkinter.messagebox.showinfo("Guess not in range!", f"{name}, your guess is not in the range of possible numbers.")
      else:
        if guess < number: tkinter.messagebox.showinfo("Guess lower than number!", f"{name}, your guess is lower than the number.")
        elif guess > number: tkinter.messagebox.showinfo("Guess higher than number!", f"{name}, your guess is higher than the number.")
        elif guess == number: tkinter.messagebox.showinfo("Correct!", f"{name}, you guessed correctly! The number was {number}.")
    else: tkinter.messagebox.showinfo("No name!", "Please enter a name to guess.")
  else: tkinter.messagebox.showinfo("No guess!", "Please enter a number to guess.")


Label(window, text = "Guess The Number!", width = 16).place(x = 104, y = 4)

Label(window, text = "Enter your name:", width = 16).place(x = 4, y = 54)
enterName = Entry(window, width = 16)
enterName.place(x = 204, y = 54)

Button(window, text = "Confirm name", width = 16, command = confirmName).place(x = 104, y = 84)

Label(window, text = "Guess the number:", width = 16).place(x = 4, y = 134)
enterNumber = Entry(window, width = 16)
enterNumber.place(x = 204, y = 134)

Button(window, text = "Confirm choice", width = 16, command = confirmChoice).place(x = 104, y = 164)


window.mainloop()