from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("350x200")
window.title("Temperature Converter")
window.config(background = "#ECF2F5")

customFont = font.Font(family = "Times", size = 12, weight = "bold")


titleLabel = Label(window, text = "Temperature Converter\n°C -> °F or °F -> °C", font = customFont)
titleLabel.pack()

frame = Frame(window)
frame.pack()

unitPickerLabel = Label(frame, text = "Enter Unit", font = customFont)
unitPickerLabel.grid(row = 2, column = 1)

enterTemperatureLabel = Label(frame, text = "Enter Temperature", font = customFont)
enterTemperatureLabel.grid(row = 2, column = 3)

unitPicker = Entry(frame, font = customFont, width = 10)
unitPicker.grid(row = 3, column = 1)

Scrollbar(frame).grid(row = 3, column = 2)

enterTemperature = Entry(frame, font = customFont, width = 10)
enterTemperature.grid(row = 3, column = 3)

units = {
  "Celsius": "°F",
  "Fahrenheit": "°C"
}

def convert():
  selectedUnit = unitPicker.get()
  enteredTemperature = int(enterTemperature.get())

  if selectedUnit == "Celsius": newTemperature = enteredTemperature * (9 / 5) + 32
  else: newTemperature = (enteredTemperature - 32) / (9 / 5)

  newTemperature *= 10
  newTemperature //= 1
  newTemperature /= 10
  
  outputLabel = Label(frame, text = f"{newTemperature}{units[selectedUnit]}", font = customFont)
  outputLabel.grid(row = 5, column = 2)

convertButton = Button(frame, text = "Convert", command = convert, font = customFont).grid(row = 4, column = 2)


window.mainloop()