# Trong Python ko co muc truy cap chinh thuc nhu public, protected, private ma dung
"""
self.    : public - dung o dau cung dc
self._   : protected - chi dung trong  package
self.__  : private - chi dung trong cung class
"""

# vi du cu the nhu sau
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # tao 1 thuoc tinh protected
        self._school = "Ly Thai To"

        # tao 1 thuoc tinh private - grade
        self.__grade = 0            # gan gia tri ban dau mac dinh

# cach truy cap thi phai dung getter/ setter : dung trong cung class
    def set_grade(self, value):
        if 0 <= value <= 10:
            self.__score = value
        else:
            print("Diem ko hop le")

    def get_grade(self):
        return self.__score

s = Student('Thuan', 17)
print(s.name)
print(s._school)
# print(s.__grade) cau leh nay se loi

print(s.set_grade(9))
print(s.get_grade())

