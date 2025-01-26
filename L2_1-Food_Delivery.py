from tkinter import *
from tkinter.ttk import *
import time

window: Tk = Tk(); window.title("Food Delivery App"); window.geometry("200x165"); window.config(background = "#444444")

def order():
  for widget in orderWidgets: widget[0].place(x = widget[1][0], y = widget[1][1])

def enterDetails():
  for widget in detailWidgets: widget[0].place(x = widget[1][0], y = widget[1][1] + 55)

def bar():
  progressBar = Progressbar(window, length = 400)
  progressBar.pack()
  
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

  Label(window, text = "Done!").place(x = 80, y = 130)

orderWidgets = [[Label(window, text = "Food:"), [5, 5]], [Entry(window), [45, 5]], [Button(window, text = "Continue", command = enterDetails), [5, 30]]]
detailWidgets = [[Label(window, text = "Name:"), [5, 5]], [Entry(window), [45, 5]], [Button(window, text = "Order", command = bar), [5, 30]]]

menubar = Menu(window)
menubar.place()

orderButton = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Order", menu = orderButton)
orderButton.add_command(label = "Order", command = order)
orderButton.add_separator()
orderButton.add_command(label = "Support")

window.config(menu = menubar)
window.mainloop()