# tao 1 lop cha Animal co 2 thuoc tinh name, age va 1 phthuc speak
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass           # Moi loai dong vat keu khac nhau

# ke thua trong Python ko dung tu extends ma dung nhu sau
class Dog(Animal):
    def speak(self):
        return f"I'm {self.name} and {self.age} years old. Wolf wolf!!"

    def FoodFav(self):
        print("I love Jollibe and KFC")

#tuong tu co the tao cat, duck,... thay doi phuong thuc speak

# tao doi tuong
dog1 = Dog("Mark",10)
print(dog1.speak())
dog1.FoodFav()


# lam ro hon ham khoi tao __init__() function:
class Person:      # Parent
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def info(self):
        return f"My name is {self.name} and my id is {self.idnumber}"

class Employee(Person):     # Ke thua Person - Child
    # lop con co the co ham khoi tao- them thuoc tinh, hanh vi rieng
    def __init__(self, name, idnumber, salary, post):
        # vi Parent co name va idnumber -> super
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post

    def info(self):
        return f"Hello I'm {self.name} and my post is {self.post}"

# doi tuong lop cha
Marry = Person("Marry", 2222)
print(Marry.info())

# doi tuong lop con
Emp1 = Employee("John",1000,"$500", 211)
print(Emp1.info())

#con nhieu kieu ke thua nx :v kho ghe
# 1 lop con ke thua 1 lop cha : nhu o tren
# 1 lop con ke thua nhieu lop cha :
# Cac lop con < cha < ong : Ke thua nhieu cap
# nhieu lop con ke thua 1 lop cha
# co the gop 4 loai ke thua tren (hybird)

