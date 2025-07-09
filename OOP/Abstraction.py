from abc import ABC, abstractmethod

# trong python co module abc = abstract Class
# va moudle ABstract Method

# dinh nghia 1 lop truu tuong nhu sau
class Animal(ABC):      # Ke thua lop ABC tu module abc
    @abstractmethod
    def sound(self):
        pass

    @property
    @abstractmethod
    def species(self):
        pass
# 1 lop con khi ke thua 1 lop cha se thuc hien moi hanh vi cua abc do
# phai dinh nghia phuong thuc do
class Dog(Animal):
    # dinh nghia lai phuong thuc trong lop truu tuong
    def sound(self):
        return "Wolf Wolf Wolf!"

    def species(self):
        return "Cannie"

# tao doi tuong dog1 goi ham thong qua ten lop
dog1 = Dog()
print(dog1.sound())
print(dog1.species())
