class human:

   def __init__(self, name, age):
      self.name = name
      self.age = age
      print(f"Human Object Created. Name: {self.name}, Age: {self.age}.")

   def getName(self):
      print(self.name)

   def getAge(self):
      print(self.age)


class contractor(human):
   pass

bill = contractor("bill", 56)

adam = human("Adam", 100)

adam.getName()
adam.getAge()
bill.getName()
bill.getAge()