'''
print(1+3)  # 4
print("appna" + "College")  # concatenate
print([1, 2, 3] + [4, 5, 6])  # merge
'''

# Operator and Dunder Overloading
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)



num1 = complex(4, 5)
num1.showNum()

num2 = complex(-1, 3)
num2.showNum()

num3 = num1.add(num2)
num3.showNum()