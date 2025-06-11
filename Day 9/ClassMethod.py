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