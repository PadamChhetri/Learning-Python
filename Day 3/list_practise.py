'''
#Wap to ask user to enter names of their 3 favourite movies and store them in list
movie=[]
mov1=input("Enter a first movie name:")
mov2=input("Enter a second movie name:")
mov3=input("Enter a third movie name:")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print(movie)
'''

#Wap to check if a list contains palindrome of elements.
list=[1,2,3,2,1]
copy=list.copy()
copy.reverse()

if(copy == list):
  print("It is palindrome")
else:
  print("It is not palindrome")

  
