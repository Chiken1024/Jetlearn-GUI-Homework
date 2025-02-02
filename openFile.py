from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

window: Tk = Tk()
window.geometry("200x200")

def saveFile():
  files: list = [("All Files", "*.*"), ("Python Files", "*.py"), ("Text Documents", "*.txt")]
  asksaveasfile(filetypes = files, defaultextension = files)

Button(window, text = "Open File", command = saveFile).pack(pady = 80)

window.mainloop()