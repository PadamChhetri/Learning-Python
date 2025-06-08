class car:
  def __init__(self):
    self.acc= False
    self.brk=False
    self.clautch=False

  def start(self):
    self.acc= True
    self.clautch=True
    print("Car Start")
car1=car()
car1.start()
