from tkinter import *

windowSize: list = [400, 400]
window: Tk = Tk(); window.title("Spinbox"); window.geometry(f"{windowSize[0]}x{windowSize[1]}"); window.config(background = "#442222")

Spinbox(window, from_ = -10, to = 10).pack()

window.mainloop()