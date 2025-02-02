class Student:
  def __init__(self, name: str, age: int) -> None:
    self.name: str = name
    self.age: int = age
  
  def listDetails(self) -> None: print(f"Student {self.name} is {self.age} years old.")

martin: Student = Student("Martin", 14)
martin.listDetails()