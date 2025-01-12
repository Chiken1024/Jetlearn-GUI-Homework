from tkinter import *

windowSize: list = [256, 256]

window: Tk = Tk(); window.title("Menu Bar"); window.geometry(f"{windowSize[0]}x{windowSize[1]}"); window.config(background = "#442222")

menubar = Menu(window)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = file)
file.add_command(label = "New File")
file.add_command(label = "New Window")
file.add_separator()
file.add_command(label = "Open")
file.add_command(label = "Save")
file.add_separator()
file.add_command(label = "Exit", command = window.destroy)

edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = edit)
edit.add_command(label = "Undo")
edit.add_command(label = "Redo")
edit.add_separator()
edit.add_command(label = "Cut")
edit.add_command(label = "Copy")
edit.add_command(label = "Paste")
edit.add_separator()
edit.add_command(label = "Find")
edit.add_command(label = "Replace")

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = help)
help.add_command(label = "Guide")
help.add_command(label = "Release Notes")
help.add_separator()
help.add_command(label = "Keyboard Shortcuts")
help.add_command(label = "About")

window.config(menu = menubar)

window.mainloop()