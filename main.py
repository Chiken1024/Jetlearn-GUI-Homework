from tkinter import *
import tkinter.font as tkfont
import random

window = Tk()
window.geometry("395x180")
window.title("Rock Paper Scissors")
window.config(background = "#88aacc")

font = tkfont.Font(family = "Helvetica", size = 12, weight = "bold")


playerChoice = ""
computerChoice = ""

def playerChoseRock():
  global playerChoice
  playerChoice = 0
  
  playerChose()

def playerChosePaper():
  global playerChoice
  playerChoice = 1
  
  playerChose()

def playerChoseScissors():
  global playerChoice
  playerChoice = 2
  
  playerChose()

def playerChose():
  global playerChoice, computerChoice

  computerChoice = random.randint(0, 2)

  playerChoiceDisplay.config(text = options[playerChoice])
  computerChoiceDisplay.config(text = options[computerChoice])

  decideWinner()

def decideWinner():
  global playerChoice, computerChoice

  if playerChoice == computerChoice: winnerDisplay.config(text = "Draw!")
  elif computerChoice == (playerChoice + 1) % 3: winnerDisplay.config(text = "Computer Wins!")
  elif playerChoice == (computerChoice + 1) % 3: winnerDisplay.config(text = "Player Wins!")


options = ["Rock", "Paper", "Scissors"]

title = Label(window, text = "Rock Paper Scissors", font = font, background = "#88aacc")
title.grid(row = 0, column = 0)

playerFrame = Frame(window, background = "#6688aa")
playerFrame.grid(row = 1, column = 0)

playerPickChoice = Label(playerFrame, text = "Pick your choice:", font = font, background = "#88aacc", width = 15)
playerPickChoice.grid(row = 0, column = 0)

Button(playerFrame, text = options[0], font = font, width = 7, background = "#6688aa", activebackground = "#446688", command = playerChoseRock).grid(row = 0, column = 1)
Button(playerFrame, text = options[1], font = font, width = 7, background = "#6688aa", activebackground = "#446688", command = playerChosePaper).grid(row = 0, column = 2)
Button(playerFrame, text = options[2], font = font, width = 7, background = "#6688aa", activebackground = "#446688", command = playerChoseScissors).grid(row = 0, column = 3)

playerChoiceLabel = Label(playerFrame, text = "Your choice:", font = font, background = "#88aacc", width = 15)
playerChoiceLabel.grid(row = 1, column = 0)

playerChoiceDisplay = Label(playerFrame, text = "No option selected yet.", font = font, background = "#6688aa")
playerChoiceDisplay.grid(row = 1, column = 1, columnspan = 3)

winnerLabel = Label(playerFrame, text = "Winner:", font = font, background = "#88aacc", width = 15)
winnerLabel.grid(row = 2, column = 0, pady = 8)

winnerDisplay = Label(playerFrame, text = "No winner yet.", font = font, background = "#88aacc")
winnerDisplay.grid(row = 2, column = 1, columnspan = 3)

computerFrame = Frame(window, background = "#6688aa")
computerFrame.grid(row = 3, column = 0)

computerChoiceLabel = Label(computerFrame, text = "Computers choice:", font = font, background = "#88aacc", width = 15)
computerChoiceLabel.grid(row = 0, column = 0)

computerChoiceDisplay = Label(computerFrame, text = "No option selected yet.", font = font, background = "#6688aa")
computerChoiceDisplay.grid(row = 0, column = 1, columnspan = 3)

computerPickChoice = Label(computerFrame, text = "Computer choice:", font = font, background = "#88aacc", width = 15)
computerPickChoice.grid(row = 1, column = 0)

Button(computerFrame, text = options[0], font = font, width = 7, background = "#6688aa", state = "disabled").grid(row = 1, column = 1)
Button(computerFrame, text = options[1], font = font, width = 7, background = "#6688aa", state = "disabled").grid(row = 1, column = 2)
Button(computerFrame, text = options[2], font = font, width = 7, background = "#6688aa", state = "disabled").grid(row = 1, column = 3)


window.mainloop()