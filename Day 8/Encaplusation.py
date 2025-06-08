#Create account class with 2 attributes -balance and account no. Create method of debit,credit and printing the balance
class Account():
  def __init__(self,bal,acc):
    self.bal=bal
    self.acc=acc
  
  #debit method
  def debit(self,amount):
    self.bal-=amount
    print("Rs",amount,"was debited")
    print("tOAL balance=",self.get_balance())

  #Credit method
  def credit(self,amount):
    self.bal+=amount
    print("Rs",amount,"was credited")
    print("tOAL balance=",self.get_balance())

  def get_balance(self):
    return self.bal

acc1=Account(10000,12345)
acc1.debit(100)
acc1.credit(500)
