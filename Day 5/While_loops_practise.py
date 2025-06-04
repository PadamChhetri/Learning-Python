'''
#Print from 10 to 1 
i=10
while i >= 1:
  print(i)
  i -=1


#Print from 1 to 10 
i=1
while i <= 10:
  print(i)
  i +=1


#Print multiplication number from a number n
i=1
n=int(input("Enter a number:"))
while i<=10:
  mul=n*i
  print(mul)
  i+=1


#print the following list 
nums=[5,74,46,8451,56,2315,315]
i=0
while i <= len(nums)-1:
 print(nums[i])
 i+=1
'''

'''
#search for the number x in the tuple using loop
nums=(5,74,46,8451,56,2315,315,46)
x=46
i=0 #initialization
while i < len(nums): #condition
  if(nums[i]==x):
    print("Found value at idx",i)
  else:
    print("not found")
  i+=1
'''

'''
#find the sum of first n numbers
n=5
sum=0
i=1
while i <= n:
  sum+=i
  i += 1  # increment step
print("The sum of number is:",sum)
'''

#Find the factorial of firt n number
n=5
i=1
fact=1
while (i<=n):
  fact*=i
  i+=1
print("factorial number is:",fact)

