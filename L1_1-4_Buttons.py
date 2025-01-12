from tkinter import *

#----#
windowSize: list = [256, 256]
padding: int = 8
#----#

window: Tk = Tk(); window.title("L1_1-4_Buttons"); window.geometry(f"{windowSize[0]}x{windowSize[1]}"); window.config(background = "#442222")
corners: list = [[padding, padding], [padding, windowSize[1] - padding - 70], [windowSize[0] - padding - 64, padding], [windowSize[0] - padding - 64, windowSize[1] - padding - 70]]
for i in range(4): Button(window, text = i, width = 8, height = 4, bg = "#882222").place(x = corners[i][0], y = corners[i][1])
window.mainloop()