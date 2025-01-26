from tkinter import *

window: Tk = Tk(); window.title("L1_1-4_Buttons"); window.geometry("400x400"); window.config(background = "#222222")

frame1 = Frame(window)
frame1.pack(side = LEFT)
frame1Buttons = ["1", "2", "3"]
for frame1Button in frame1Buttons: Button(frame1, text = frame1Button).pack()

frame2 = Frame(window)
frame2.pack(side = RIGHT)
frame2Buttons = ["x", "y", "z"]
for frame2Button in frame2Buttons: Button(frame2, text = frame2Button).pack()

frame3 = Frame(window)
frame3.pack(side = TOP)
frame3Buttons = ["a", "b", "c"]
for i in range(6, 9): Label(frame3, text = frame3Buttons[i - 6], bg = f"#{i}f{i}f{i}f").pack()

window.mainloop()