'''
#Read to a file
f = open("demo1.txt", "r") #Open for reading
data = f.read()
# line=f.readline() #Read one line at a time
print(data)
f.close()  
'''

#Write to a file
# f=open("demo.txt","w") #Create a new demo.txt file and weite the text
# f.write("Hello")
# f.close()

#OR
# f=open("demo.txt","a") #add txt in a existing or if not create a file
# f.write("\nwelcome")
# f.close()

'''
f=open("demo1.txt","r+")
f.write("abc") #overwirte abc from starting of file
data=f.read()
print(data)
f.close()
'''

'''
f=open("demo1.txt","w+")
f.write("abc") #trauncate(delete) all and write abc
data=f.read()
print(data)
f.close()
'''


f=open("demo1.txt","a+")
f.write("abc") #append new abc at the end
data=f.read()
print(data)
f.close()