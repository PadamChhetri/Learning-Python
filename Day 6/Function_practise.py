'''
#WAF to find the length of the list 
num=[8,1,2,3,23,15]
cities=["london","Kathmandu"]

def print_len(list):
  length=len(list)
  print(length)
print_len(num)
print_len(cities)
'''

'''
#WAF to print the elements of a list in  a single line   
l=["Hello", "World","Welcome","Man"]

def print_line(list):
  for i in list:
    print(i, end=" ") 
  print_line(l)
'''

'''
#WAF to print the factorial of n number
def cal_fact(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  print("Final factorial:", fact)
  return fact
# Call the function
cal_fact(5)

#using while loop
def cal_fact(n):
  fact=1
  i=1
  while (i<=n):
    fact=fact*i
    i+=1
  print(fact)
  return fact

cal_fact(5)
'''

'''
#WAF to convert usd to npr
def cal_convertor(usd_val):
  npr_val=usd_val*87
  print(usd_val,"USD=",npr_val,"NPR")
  return cal_convertor
cal_convertor(7000)
'''

#WAF to to check whether number is odd or even and return in string odd or even
def check_odd_even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
    
# Example usage
result = check_odd_even(7)
print(result) 