from tkinter import *

window: Tk = Tk()
window.geometry("350x200")
window.title("Temperature Converter")


titleLabel = Label(window, text = "Temperature Converter\n°C -> °F or °F to °C")
titleLabel.pack()

frame = Frame(window)
frame.pack()

unitPickerLabel = Label(frame, text = "Enter Unit")
unitPickerLabel.grid(row = 2, column = 1)

enterTemperatureLabel = Label(frame, text = "Enter Temperature")
enterTemperatureLabel.grid(row = 2, column = 3)

unitPicker = Entry(frame)
unitPicker.grid(row = 3, column = 1)

Scrollbar(frame).grid(row = 3, column = 2)

enterTemperature = Entry(frame)
enterTemperature.grid(row = 3, column = 3)

units = {
  "Celsius": "°F",
  "Fahrenheit": "°C"
}

def convert():
  selectedUnit = unitPicker.get()
  enteredTemperature = int(enterTemperature.get())

  if selectedUnit == "Celsius": newTemperature = enteredTemperature * (9 / 5) + 32
  else: newTemperature = enteredTemperature - 32 / (9 / 5)
  
  outputLabel = Label(frame, text = f"{newTemperature}{units[selectedUnit]}")
  outputLabel.grid(row = 5, column = 2)

convertButton = Button(frame, text = "Convert", command = convert).grid(row = 4, column = 2)


window.mainloop()