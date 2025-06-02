tuple=(54,568,489,1654,15848,)
# print(type(tupke))
# print(tuple)
# tuple[0]=456  #cannot be changed not allowed 
print(tuple[1:2])
print(tuple[::2]) #means use a step of 2 — skip every other element.
print(tuple[2:])
print(tuple[-3:-1])

# Index of its first occurrence
index=tuple.index(54)
print(index)

# Counting the number of times a value appears in the tuple
print(tuple.count(568))

