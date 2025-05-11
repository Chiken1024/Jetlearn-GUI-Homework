from tkinter import *
import tkinter.font as tkfont

class Game:
  def __init__(self) -> None:
    self.WINDOW_SIZE: tuple[int] = (360, 440)
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
    
    self.FONT = tkfont.Font(self.window, font = "consolas", size = 16)
  
  def run(self) -> None:
    self.playButton = Button(self.window, bg = self.PALETTE["foreground"], highlightcolor = self.PALETTE["highlighted"], text = "Play", font = self.FONT, command = self.play)
    self.playButton.pack(anchor = CENTER)
  
  def play(self) -> None:
    self.playButton.destroy()
    
    def getGrid() -> list[str]: return [self.buttons[i]["text"] for i in range(9)]

    self.lines: list[list[int]] = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def gameOver(winner: str) -> None:
      Label(self.gameFrame, fg = self.PALETTE["highlighted"], bg = self.PALETTE["background"], text = f"{winner} has won!", font = self.FONT).grid(row = 4, column = 0, columnspan = 3)
      self.buttonPressEnabled = False

    def update() -> None:
      grid: list[str] = getGrid()

      for line in self.lines:
        if grid[line[0]] == ".": break
        for i in range(2):
          if grid[line[i]] != grid[line[i + 1]]: break
        else: gameOver(grid[line[0]])
      
      for tile in grid:
        if tile == ".": break
      else:
        if self.buttonPressEnabled: gameOver("Nobody")
      
      if self.currentTurn == "X": self.currentTurn = "O"
      else: self.currentTurn = "X"

    self.buttonPressEnabled: bool = True

    def buttonPressed(button: int) -> None:
      if self.buttonPressEnabled and self.buttons[button]["text"] == ".":
        self.buttons[button].config(background = self.PALETTE["highlighted"], text = self.currentTurn)
        update()

    def button1() -> None: buttonPressed(0)
    def button2() -> None: buttonPressed(1)
    def button3() -> None: buttonPressed(2)
    def button4() -> None: buttonPressed(3)
    def button5() -> None: buttonPressed(4)
    def button6() -> None: buttonPressed(5)
    def button7() -> None: buttonPressed(6)
    def button8() -> None: buttonPressed(7)
    def button9() -> None: buttonPressed(8)

    self.buttonCommands: list[function] = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    self.gameFrame: Frame = Frame(self.window, bg = self.PALETTE["background"])
    self.gameFrame.pack(anchor = CENTER, pady = 20)

    titleLabel: Label = Label(self.gameFrame, bg = self.PALETTE["highlighted"], fg = self.PALETTE["text"], text = "Tic Tac Toe!", font = self.FONT)
    titleLabel.grid(row = 0, column = 0, columnspan = 3)

    self.buttons: list[Button] = []
    for i in range(9):
      self.buttons.append(Button(self.gameFrame, bg = self.PALETTE["foreground"], fg = self.PALETTE["text"], highlightbackground = self.PALETTE["highlighted"], width = 8, height = 4, text = ".", font = self.FONT, command = self.buttonCommands[i]))
      self.buttons[-1].grid(row = i % 3 + 1, column = i // 3)
    
    self.currentTurn = "X"

if __name__ == "__main__":
  game: Game = Game()
  game.run()
  game.window.mainloop()