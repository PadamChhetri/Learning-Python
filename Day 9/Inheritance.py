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

