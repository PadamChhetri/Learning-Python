'''
dict={
  "table" : ["a piece of furniture","list of facts and figures"],
  "cat" : "a small animal"
}
print(dict)
'''

#Wap to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.
'''
dict={}
sub1=input("enter a first subject:")
sub2=input("enter a second subject:")
sub3=input("enter a third subject:")

dict["chemistry"]=sub1 
dict["physics"]=sub2
dict["math"]=sub3

print(dict)
'''

#or
dict={}
sub1=input("enter a first subject:")
dict.update({"chemistry":sub1 })
sub2=input("enter a second subject:")
dict.update({"phyics":sub2 })
sub3=input("enter a third subject:")
dict.update({"math":sub3 })


print(dict)