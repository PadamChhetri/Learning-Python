'''
def is_prime(n):
    if n <= 1:
        return False  # not a prime number
    for i in range(2, n):  # check from 2 to n-1
        if n % i == 0:
            return False   # divisible by other number, not prime
    return True            # no divisors, it's prime
print(is_prime(4))




def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                return
        print(n,"is a prime number")
    else:
        print(n," is not a prime number")

is_prime(5)


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

    

def is_prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if (n % i == 0):
            return False
        return True
    
numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]

# Get only prime numbers from the list
prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime numbers in the list:", prime_numbers)       
'''