dict={
  "name": "Padam",
  "age": 21,
  "college":"Orchid International College",
  "subject" : ["python","C++"],
  "topics" : ("Dictionary","set"),
  "is_adult": True,
  "cgpa" : 91.5
}
print(dict["name"])  # Access value using the key

dict["name"]="Adam" #can be changed(overwrite) and it is mutable(changable) 
dict["surname"]="Chhetri" #can add key and value 
print(dict)

# Remove a key-value pair
# del dict['college']
# print(dict)

# Remove using pop
# dict.pop('subject')
# print(dict)


'''
#Strated with empty dictionary
null_dist={}
null_dist["name"]="shyam"
print(null_dist)
'''

