#dinh nghia 1 class cu the
class testClass:
    # chua cac bien
    variable = 10
    control = -12.19
    name = "Hello thuan"

    # chua ham ( kieu truy cap mac dinh)
    def InfoDef(self):
        print("This func is in class")

# su dung ham thong qua ten class
## tao 1 doi tuong
myclass = testClass()
myclass.InfoDef()

## truy cap thuoc tinh( bien cua doi tuong)
print(myclass.variable)

## co the thay doi thuoc tinh cua doi tuong
myclass.variable = 21
print(myclass.variable)


# ham khoi tao __init__ ( giong constructor)
class NumberHolder:
    def __init__(self, number):     ## chi co 1 thuoc tinh ( giong dung tu khoa this)
        self.number = number

    def returnNumber(self):
        return self.number

## cach dung nhu sau
var2 = NumberHolder(10)     ## da tao 1 ham gan khoi tao thuoc tinh cho doi tuong
print(var2.returnNumber())

# mot vi du khac
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):     # co 2 thuoc tinh
        self.name = name
        self.age = age  # Instance attribute

    def bark(self):
        print("wolf wolf wolf!")

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

# tu khoa self giup truy cap thuoc tinh, phuong thuc cua doi tuong thong qua ten
print(dog1.name, dog1.species, dog1.age)
dog1.bark()