'''
#Odd number or even number
number=int(input("Enter a number:"))

if(number % 2==0):
  print("even number")
else:
  print("Odd number")

'''
'''
#greatest of 3 numbers entered by a user
number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
number3=int(input("Enter third number:"))

if(number1 >= number2 and number1 >= number2 ):
  print(" Number1 is Greatest number",number1)
elif(number2 >= number3):
    print(" Number2 is Greatest number",number2)
else:
  print(" Number3 is Greatest number",number3)
'''


#Multiple of 7 or not
number=int(input("Enter the number:"))
if(number % 7 ==0):
  print("Multiple of 7")
else:
  print("is not multiple of 7")
