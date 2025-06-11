class car:
  def __init__(self,type):
    self.type=type

  @staticmethod
  def start():
    print("car strated")

  @staticmethod
  def stop():
    print("Stop")

class Toyota(car):
  def __init__(self,name,type):
    self.name=name
    super().__init__(type) #call parent class constructor
    super().start()

car1=Toyota("pirus","Electric")
print(car1.type)