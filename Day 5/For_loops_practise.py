#Print the elements of the following list
list=[1,4,9,16,36,49,64,81,100]
for val in list:
  print(val)

#search in the number x in tuple using loop
tup=(1,4,9,16,36,49,64,81,100)
x=36
#idx=0  #to find the number in which index
for val in tup:
  if(val==x):
  #   print("found at index",idx)
  # idx+=1 # for index
    print("found",x)
    break
  else:
    print("not found")

