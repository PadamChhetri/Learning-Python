
#Nested Dictionary
student =  {
  "name":"Padam",
  "subject":  {
    "Math" : 89,
    "Python" : 91
  }
}
print(student)

'''
print(student["subject"])
print(student["subject"]["Math"])
print(list(student.keys())) #Typecasting dictionary keys into list
print(len(student)) #know the length of keys 

print(student.values())
print(list(student.values())) #Typecasting dictionary values into list

print(list(student.items()))  #returns all {key and values} pairs as tuples
pairs=(list(student.items()))
print(pairs[0])#returns all {key} as tuples
print(pairs[1])#returns all {values} as tuples
'''

# print(student["name1"]) #error after this another code will not execute
print(student.get("name1")) # no error --> None after this another code will execute

# new_dict=student.update({"city" : "Kathmandu","age":22}) #or

new_dict=({"city" : "Kathmandu","age":22})
student.update(new_dict)
print(student)