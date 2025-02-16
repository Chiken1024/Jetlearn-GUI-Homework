from tkinter import *
import calendar


def getCalendar():
  calendarWindow = Tk()
  calendarWindow.geometry("300x300")
  calendarWindow.title("Calendar")
  calendarWindow.config(background = "#222244")


  year = int(selectYear.get())
  calendarContent = calendar.calendar(year)

  calendarLabel = Label(calendarWindow, text = calendarContent, background = "#666688")
  calendarLabel.place(x = 90, y = 5)


  calendarWindow.mainloop()


if __name__ == "__main__":
  window = Tk()
  window.geometry("213x90")
  window.title("Get Calendar")
  window.config(background = "#222244")


  selectYearLabel = Label(window, text = "Select year:", background = "#666688").place(x = 5, y = 5)

  selectYear = Spinbox(window, from_ = 1925, to = 2025, width = 20, background = "#666688")
  selectYear.place(x = 73, y = 5)

  getCalendarButton = Button(window, text = "Get calendar", command = getCalendar, background = "#666688").place(x = 67.5, y = 30)
  exitButton = Button(window, text = "Exit", command = exit, background = "#884444").place(x = 90, y = 60)


  window.mainloop()
