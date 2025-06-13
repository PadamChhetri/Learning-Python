'''
#Create a circle class with radius r using constructor. Define an Area() and Perimeter() Method of the class and calculate area and perimeter 
class circle:
  def __init__(self,radius,):
    self.radius=radius
    #Method
  def Area(self):
    return (22/7)*self.radius ** 2
  
  def Perimeter(self):
    return 2*(22/7)*self.radius
  
c1=circle(21)
print(c1.Area())
print(c1.Perimeter())
'''


'''
class Employee:
  def __init__(self,role,dept,salary):
    self.role=role
    self.dept=dept
    self.salary=salary

  def showDetails(self):
    print("role = ",self.role)
    print("department = ",self.dept)
    print("Salary = ",self.salary)

class Engineer(Employee): #Inherit from Employee
  def __init__(self,name,age):
    self.name=name
    self.age=age
    super().__init__("Engineer","IT",75000)

Eng1=Engineer("Padam",22)
Eng1.showDetails()
'''

#Use Dunder function that order 1 is greater than order 2
class order:
  def __init__(self,item,price):
    self.item=item
    self.price=price

  def __gt__(self,ord2):
    return self.price > ord2.price

odr1=order("Chipes",20)
odr2=order("nOODLES",22)

print(odr1>odr2)
  