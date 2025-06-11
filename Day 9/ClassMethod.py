#Class Method
'''
#Class Method
class Person:
  name="Padam"

  # def chagename(self,name):
  #   self.__class__.name=name

  @classmethod
  def changename(cls,name):
    cls.name=name

p1=Person()
p1.chagename("Adam")

print(p1.name)
print(Person.name)
'''

#Property Decorator
class Student:
  def __init__(self,phy,chem,math):
    self.phy=phy
    self.chem=chem
    self.math=math

  @property
  def percentage(self):
    return str((self.phy + self.chem + self.math)/3) + "%"
stu1=Student(91,98,91)
print(stu1.percentage)

stu1.phy=99
print(stu1.percentage)
