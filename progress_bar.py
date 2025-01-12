from tkinter import *
from tkinter.ttk import *
import time

windowSize: list = [400, 400]
window: Tk = Tk(); window.title("Progress Bar"); window.geometry(f"{windowSize[0]}x{windowSize[1]}"); window.config(background = "#442222")

def bar():
  progressBar["value"] = 0
  window.update_idletasks()
  time.sleep(0.5)
  
  progressBar["value"] = 20
  window.update_idletasks()
  time.sleep(1)

  progressBar["value"] = 40
  window.update_idletasks()
  time.sleep(1)

  progressBar["value"] = 50
  window.update_idletasks()
  time.sleep(1)

  progressBar["value"] = 65
  window.update_idletasks()
  time.sleep(1)

  progressBar["value"] = 98
  window.update_idletasks()
  time.sleep(4)

  progressBar["value"] = 100
  window.update_idletasks()

progressBar = Progressbar(window, length = 400)
progressBar.pack()

startProgress = Button(window, text = "Start Bar", command = bar).pack()

window.mainloop()