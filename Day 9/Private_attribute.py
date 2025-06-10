#Private atribute is meant to be used only within the class and are not accessible from outside the class
'''
class Account:
  def __init__(self,acc_no, acc_pass):
    self.acc_no=acc_no #Public attributes
    self.__acc_pass=acc_pass #Private attributes

  def reset_pass(self):
    print(self.__acc_pass) # # accessing private attribute inside the class



acc1=Account("12345","acd")
print(acc1.acc_no)
print(acc1.reset_pass())
'''

class person:
  __name="Anonymous"

  def __hello(self):
    print("Hello")

  def welcome(self):
    self.__hello()

p1=person()
print(p1.welcome())