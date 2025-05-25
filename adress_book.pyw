from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile


class Main:
  def __init__(self) -> None:
    self.WINDOW_SIZE: tuple[int, int] = (360, 245)
    
    self.window: Tk = Tk()
    self.window.title("L1_1-4_Buttons")
    self.window.geometry(f"{self.WINDOW_SIZE[0]}x{self.WINDOW_SIZE[1]}")

  def run(self) -> None:
    self.adresses: dict[str, dict[str, str]] = {}
    
    def open() -> None:
      fileIn: None = askopenfile(title = "Open File")

      if fileIn:
        items = fileIn.readlines()
        for item in items: self.adresses.update(dict(item))
        
        adresses.delete(0, END)
        for adress in self.adresses: adresses.insert(END, adress["name"])
    
    

    def edit() -> None: pass

    def delete() -> None: adresses.delete(0, END) if adresses.curselection() == () else adresses.delete(adresses.curselection())

    def add() -> None:
      self.adresses.update({entries[0].get(): {labels[i]: entries[i].get() for i in range(0, 5)}})
      
      adresses.insert(END, self.adresses[entries[0].get()]["Name:"])

    def save() -> None:
      if self.adresses != {}:
        fileOut: None = asksaveasfile(defaultextension = ".txt")
        if fileOut:
          print(self.adresses)
          for item in self.adresses: print("{\"" + item + "\": " + str(self.adresses[item]) + "}", file = fileOut)
        else: raise Exception("File creation failed.")
      else: raise Exception("No adresses to save.")
    
    Label(self.window, text = "My Adress Book").grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

    Button(self.window, text = "Open", width = 27, command = open).grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5)

    adresses: Listbox = Listbox(self.window)
    adresses.grid(row = 1, column = 0, rowspan = 5, columnspan = 2, padx = 5, pady = 5)

    #for i in range(4): adresses.insert(END, i)  # Temporary

    labels: list[str] = ["Name:", "Adress:", "Mobile:", "Email:", "Birthday:"]
    entries: list[Entry] = []
    for i in range(5):
      Label(self.window, text = labels[i]).grid(row = i + 1, column = 2, padx = 5, pady = 5)
      entries.append(Entry(self.window))
      entries[-1].grid(row = i + 1, column = 3, padx = 5, pady = 5)
    
    labels2: list[str] = ["Edit", "Delete", "Add", "Save"]
    commands: list[function] = [edit, delete, add, save]
    for i in range(4): Button(self.window, text = labels2[i], width = 8 + i // 3 * 8, command = commands[i]).grid(row = 6, column = i, columnspan = i // 3 + 1, padx = 5, pady = 5)


if __name__ == "__main__":
  main: Main = Main()
  main.run()
  main.window.mainloop()