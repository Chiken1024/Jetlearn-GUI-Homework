from tkinter import *
import tkinter.font as tkfont

class Game:
  def __init__(self) -> None:
    self.WINDOW_SIZE: tuple[int] = (400, 400)
    self.PALETTE: dict[str, str] = {
      "background": "#7c3f58",
      "foreground": "#eb6b6f",
      "highlighted": "#f9a875",
      "text": "#fff6d3"
    }

    self.window: Tk = Tk()
    self.window.title("Tic Tac Toe")
    self.window.geometry(f"{self.WINDOW_SIZE[0]}x{self.WINDOW_SIZE[1]}")
    self.window.config(bg = self.PALETTE["background"])
    
    self.FONT = tkfont.Font(self.window, font = "font.ttf", size = 16)
  
  def run(self) -> None:
    self.playButton = Button(self.window, bg = self.PALETTE["foreground"], highlightcolor = self.PALETTE["highlighted"], text = "Play", font = self.FONT, command = self.play)
    self.playButton.pack(anchor = CENTER)
  
  def play(self) -> None:
    self.playButton.destroy()

    self.gameFrame: Frame = Frame(self.window, bg = self.PALETTE["foreground"])
    self.gameFrame.pack(anchor = CENTER)

    titleLabel: Label = Label(self.gameFrame, text = "Tic Tac Toe!", font = self.FONT)
    titleLabel.grid(row = 0, column = 0, columnspan = 3)

    for i in range(9): Button(self.gameFrame, bg = self.PALETTE["foreground"], highlightcolor = self.PALETTE["highlighted"], width = 8, height = 4, text = ".", font = self.FONT).grid(row = i % 3 + 1, column = i // 3)

if __name__ == "__main__":
  game: Game = Game()
  game.run()
  game.window.mainloop()