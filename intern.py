'''
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
      print(num, "is a prime number")
else:
    print(num, "is not a prime number") #for n less than 1 
'''



# def is_prime(n):
#   if n > 1:
#       for i in range(2, n):
#           if n % i == 0:
#               print(n, "is not a prime nber")
#               break
#       else:
#         print(n, "is a prime nber")
#   else:
#         print(n, "is not a prime nber") #for n less than 1 
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# prime_numbers = [num for num in n if is_prime(num)]
# print("Prime numbers in the list:", prime_numbers)


    