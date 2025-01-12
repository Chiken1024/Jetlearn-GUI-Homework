from tkinter import *

#----#
windowSize: list = [256, 256]
#----#

window: Tk = Tk(); window.title("L1_1-4_Buttons"); window.geometry(f"{windowSize[0]}x{windowSize[1]}"); window.config(background = "#442222")
widgets = [Label(window, text = "Create your project", width = 16).place(x = 4, y = 4), Label(window, text = "Pick a template:").place(x = 4, y = 29), Entry(window, width = 12).place(x = 98, y = 29), Label(window, text = "Name your repl:").place(x = 4, y = 54), Entry(window, width = 12).place(x = 98, y = 54), Button(window, text = "Create repl", width = 23).place(x = 4, y = 79)]
window.mainloop()