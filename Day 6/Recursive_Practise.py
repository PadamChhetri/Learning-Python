'''
#WAP to calculate the sum of first n number
def cal_sum(n):
  if(n==0):
    return 1
  else:
    return cal_sum(n-1)+n
print(cal_sum(4))
'''

#WAP to print all elements in list
num=[545,4654,548,484,78]
def print_list(list,idx=0):
  if(idx == len(list)):
    return
  print(list[idx])
  print_list(list,idx+1)
  
print_list(num)
