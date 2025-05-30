'''
light=input("Enter the traffic light:")
if(light == "green"):
    print("You can go")
elif(light == "Yellow"):
  print("Look for the vechile")
elif(light == "red"):
  print("Stop")
else:
  print("Enter the correct light")
'''

'''
marks=int(input("Enter student marks:"))
if(marks >= 90):
  print("Grade of the student is A")
elif(marks >= 80 and marks < 90):
  print("Grade of the student is B")
elif(marks >= 70 and marks < 80):
  print("Grade of the student is C")
else:
  print("Grade of the student is D")

print("The Grade of the student is :",marks)
'''


#Nestning
age=int(input("Enter your age:"))
if(age >= 18):
  if(age >= 70):
    print("You cannot drive")
  else:
    print("You can drive")
else:
  print("You cannot drive")