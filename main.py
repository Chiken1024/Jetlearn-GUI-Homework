from tkinter import *
import tkinter.font as tkfont
import random

window = Tk()
window.geometry("395x180")
window.title("Rock Paper Scissors")
window.config(background = "#88aacc")

font = tkfont.Font(family = "Helvetica", size = 12, weight = "bold")


options = ["Rock", "Paper", "Scissors"]

title = Label(window, text = "Rock Paper Scissors", font = font, background = "#88aacc")
title.grid(row = 0, column = 0)

playerFrame = Frame(window, background = "#6688aa")
playerFrame.grid(row = 1, column = 0)

playerPickChoice = Label(playerFrame, text = "Pick your choice:", font = font, background = "#88aacc", width = 15)
playerPickChoice.grid(row = 0, column = 0)

playerButtons = [
  Button(playerFrame, text = "Rock", font = font, width = 7, background = "#6688aa"),
  Button(playerFrame, text = "Paper", font = font, width = 7, background = "#6688aa"),
  Button(playerFrame, text = "Scissors", font = font, width = 7, background = "#6688aa")
]
for i in range(len(playerButtons)): playerButtons[i].grid(row = 0, column = i + 1)

playerChoiceLabel = Label(playerFrame, text = "Your choice:", font = font, background = "#88aacc", width = 15)
playerChoiceLabel.grid(row = 1, column = 0)

playerChoiceDisplay = Label(playerFrame, text = "No option selected yet.", font = font, background = "#6688aa")
playerChoiceDisplay.grid(row = 1, column = 1, columnspan = 3)

winnerLabel = Label(playerFrame, text = "Winner:", font = font, background = "#88aacc", width = 15)
winnerLabel.grid(row = 2, column = 0, pady = 8)

computerFrame = Frame(window, background = "#6688aa")
computerFrame.grid(row = 3, column = 0)

computerChoiceLabel = Label(computerFrame, text = "Computers choice:", font = font, background = "#88aacc", width = 15)
computerChoiceLabel.grid(row = 0, column = 0)

computerChoiceDisplay = Label(computerFrame, text = "No option selected yet.", font = font, background = "#6688aa")
computerChoiceDisplay.grid(row = 0, column = 1, columnspan = 3)

computerPickChoice = Label(computerFrame, text = "Computer choice:", font = font, background = "#88aacc", width = 15)
computerPickChoice.grid(row = 1, column = 0)

computerButtons = [
  Button(computerFrame, text = "Rock"),
  Button(computerFrame, text = "Paper"),
  Button(computerFrame, text = "Scissors")
]
for i in range(len(computerButtons)):
  computerButtons[i].config(font = font, width = 7, background = "#6688aa", state = "disabled")
  computerButtons[i].grid(row = 1, column = i + 1)

window.mainloop()