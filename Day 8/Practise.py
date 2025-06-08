'''
#create a student class that takes name and marks of 3 students as arguments in constructor.Then create a method to print the avegrage

class Student:

  #Constructor
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks

  #Method
  def get_avg(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("hi",self.name,"Your average score is: ",sum/3)

s1=Student("Padam",[99,97,94])
# s1.get_avg()
s1.name="Tony"
s1.get_avg()
'''


'''
#Static Method
class Student:

  @staticmethod #decorator
  def hello():
    print("Hello")

s1=Student()
s1.hello()
'''

#OOPS Importance
#--Abstraction
#--Enclapsulation
#--Inheritance
#--Polymorphism

