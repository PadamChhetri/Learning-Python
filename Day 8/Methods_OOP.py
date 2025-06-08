#Methods are functions belongs to objects.
class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

    #Method
  def welcome(self):
    print("Welcome Student",self.name)
  def get_age(self):
    print("Your age ",self.age)

s1=Student("Karan",97)
s1.welcome()
s1.get_age()