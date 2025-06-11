'''
#Single Inheritance

class car: #parent class
  @staticmethod
  def start():
    print("car strated")

  @staticmethod
  def stop():
    print("Stop")

class Tyotacar(car): #Child Class
  def __init__(self,name):
    self.name=name

car1=Tyotacar("BMW")
car2=Tyotacar("lAMBO")
print(car1.start())
print(car2.name)
'''

'''
#Multi-Level Inheritance

class car: #parent class
  @staticmethod
  def start():
    print("car strated")

  @staticmethod
  def stop():
    print("Stop")

class Toyotacar(car): #Child Class
  def __init__(self,brand):
    self.name=brand

class fortuner(Toyotacar): #Child Class
  def __init__(self,type):
    self.type=type

car1=fortuner("diseal")
car1.start()
print(car1.type)
'''

'''
#Multiple inheritance
class A:
  VarA="Welcome to class A"

class B:
  VarB="Welcome to class B"

class C(A,B):
  VarC="Welcome to class C"

C1=C()

print(C1.VarA)
print(C1.VarB)
print(C1.VarC)
'''