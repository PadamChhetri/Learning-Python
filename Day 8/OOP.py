'''
class student:
  name="Padam Chhetri"
  age=22
  college="Orchid International College"

s1=student()
print(s1.name)
'''

'''
class car: #Class
  color="red"
  brand="BWM"
car1=car() #Object
print(car1.color)
print(car1.brand)
'''

'''
#Constructor
class Student:
  #Parameterized Constructor
  def __init__(self,name,age): 
    self.name=name
    self.age=age
    print("adding student name:")
  
s1=Student("Karan",25)
print(s1.name,s1.age)
s2=Student("Aran",22)
print(s2.name,s2.age)
'''

#Class and Instance Attributes
class Student:
  college_name="Orchid" #For Common college of all student
  # name="Random" #Class Attributes 

  def __init__(self,name,age): 
    self.name=name #Obj Attr > Class Attr
    self.age=age
    print("adding student name:")
  
s1=Student("Karan",25)
print(s1.name)

s2=Student("Aran",22)
print(s2.name,s2.age)

print(Student.college_name)