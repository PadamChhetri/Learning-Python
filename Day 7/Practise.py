# with open("Practise.txt","w") as f:
#   f.write("Hi Everyone\nWelcome to learning python class\n")
#   f.write("using python.\nI like programming in python")


'''
#WAF to replace all occurances of Python with Java in abobe file
with open("Practise.txt","r") as f:
  data=f.read()
  print(data)
new_data=data.replace("python","java")
print(new_data)

with open("Practise.txt","w") as f: #now overwrite above replace in Practise.py
  f.write(new_data) 

  #OR
def check_for_word():
  with open("Practise.txt","r") as f:
    data=f.read()
    print(data)
new_data=data.replace("python","java")
print(new_data)

with open("Practise.txt","w") as f: #now overwrite above replace in Practise.py
  f.write(new_data) 
check_for_word()
'''

'''
#Search if the java is existing in file or not
word="java"
with open("Practise.txt","r") as f:
  data=f.read()
  if(word in data):
    print("Found")
  else:
    print("Not found")
'''
'''
#WAF to find in which line of the file does the word "Learning" occur First. Print -1 if word not found

def Check_word():
  word="learning"
  data=True
  line_on=1
  with open("Practise.txt","r") as f:
    while data:
      data=f.readline()
      if(word in data):
        print(line_on)
        return
      line_on+=1
  return -1
print(Check_word())
'''

#From a file containing numbers seperated by comma,print the count of even number
count=0
with open("Practise copy.txt","r") as f:
  data=f.read()

  num=data.split(",")
  for i in num:
    if(int(i) % 2 == 0):
      count+=1
print(count)


