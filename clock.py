from tkinter import *
import tkinter.font as tkfont
from tkinter.ttk import Progressbar
from time import strftime

window = Tk(); window.title("L1_1-4_Buttons"); window.geometry("400x100"); window.config(background = "#222222")


label = Label(window, font = tkfont.Font(family = "Helvetica", size = 32, weight = "bold"), bg = "#444444", fg = "#888888")
label.pack(anchor = "center")

progressBar = Progressbar(window, length = 400)
progressBar.pack()

def setLabel():
  label.config(text = strftime(f"%H:%M:%S [{int(strftime("%H")) % 12}:%M %p]"))
  label.after(1000, setLabel)

  progressBar["value"] = (int(strftime("%H")) / 24 + int(strftime("%M")) / 1440 + int(strftime("%S")) / 86400) * 100
setLabel()


window.mainloop()