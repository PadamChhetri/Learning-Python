'''
set={1,2,3,"Hello","world",2,"world"} #set ignore the duplicate value
print(set)
print(len(set)) #ignore the dublicate value and get the total number of items
'''

'''
#Set Methods
collection = set() #empty set; syntax
collection.add(12) #add an elements
collection.add("Hello") #add an elements
collection.add(42) #add an elements
# collection.remove(42) #remove an elements
# collection.clear() #rempve all elements
# collection.pop() #remove random element
print(collection)
'''

#Set Methods
set1={1,2,3}
set2={3,4,5}

set=set1.union(set2) #combine both set values and return new
print(set)

set=set1.intersection(set2) #combines common values and return new 
print(set)
