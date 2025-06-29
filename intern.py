'''
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
      print(num, "is a prime number")
else:
    print(num, "is not a prime number") #for n less than 1 
'''



# def is_prime(n):
#   if n > 1:
#       for i in range(2, n):
#           if n % i == 0:
#               print(n, "is not a prime nber")
#               break
#       else:
#         print(n, "is a prime nber")
#   else:
#         print(n, "is not a prime nber") #for n less than 1 
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# prime_numbers = [num for num in n if is_prime(num)]
# print("Prime numbers in the list:", prime_numbers)


    
# class Animal:
#   def speak(self):
#     print("some sound")

# class Dog(Animal):
#   def speak(self):
#       print("bark")
# dog=Dog()
# print(dog.speak())

class car:
  def start(self):
    print("car started")
  
  def stop(self):
    print("car stoped")

class Tyotacar(car):
  def __init__(self,name):
    self.name=name
    
car1=Tyotacar("BMW")
car2=Tyotacar("lAMBO")
print(car1.start())
print(car2.name)

  
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

