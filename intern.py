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


'''
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

  

'''
class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  
  #method

  def welcome(self):
    print("welcome",self.name)
  
  def num(self):
    print("age is",self.age)

s1=student("padam",10)

print(s1.age)
print(s1.name)
'''


#Recursion Function
# def show(n):
#   if(n==0):
#     return
#   print(n)
#   show(n-1)
# show(10)

# #Factorial of given number
# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return fact(n-1)*n
# print(fact(5))

#WAP to calculate the sum of first n number
# def sum(n):
#   if n==0:
#     return 1
#   else:
#     return sum(n-1)+n
# print(sum(5))


#swap value
# a = 5
# b = 10

# temp=a
# a=b
# b=temp

# print("After swap:")
# print("a =", a)
# print("b =", b)


# #Palindrome
def is_palindrome(s):
    # Base case: if the string is empty or has 1 character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check if first and last characters are the same
    if s[0] != s[-1]:
        return False
    # Recursive call on the substring without first and last chars
    return is_palindrome(s[1:-1])

# Test examples
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("121"))    # True


def is_palindrome(s):
    if len(s) <=1:
        return True
    if s[0]!=s[-1]:
      return False

    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
  
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))  # True
# print(is_palindrome("hello"))  # False


# s="programming"
# print(s[-3:])    # 'ing'     (last 3 characters)
# print(s[:-3])    # 'Programm' (everything except last 3)
# print(s[::-1])   # 'gnimmargorP' (full reverse)
# lst = [1, 2, 3, 4, 5]
# print(lst[::-1]) # [5, 4, 3, 2, 1]
# print(s[::-2])   # 'gmaoP' (reverse, every 2nd char)

# lst = ['a', 'b', 'c', 'd', 'e', 'f']
# print(lst[2:5])   # ['c', 'd', 'e']
# print(lst[:3])    # ['a', 'b', 'c']
# print(lst[::2])   # ['a', 'c', 'e']
# print(lst[::-1])  # ['f', 'e', 'd', 'c', 'b', 'a']


