# Operator trong Python
"""
+ - * / %
// : chia lam tron xuong
** : Luy thua

> < == >= <= !=

logical : and , or , not
"""

# Identity Operators
a = 10
b = 20
c = a
num1 = "5"
num2 = 3
print(num1 * num2)

# su dung is || is not : de kiem tra co giong nhau ko
print(a is not b)
print(a is c)

# dung trong danh sach thi nhu in || not in
x = 10
y = 11

arr = [10, 100, 21, 200, 0, -10]
print(arr)
if(x not in arr):
    print(f"{x} is NOT present in arr")
else:
    print(f"{x} is present in arr")

if (y not in arr):
    print(f"{y} is NOT present in arr")
else:
    print(f"{y} is present in arr")

# toan tu 3 ngoi
a, b = 10,20
min = a if a < b else b
print(min)

# thu tu uu tien cua cac phep toan
## ** ,* ,/ ,% ,+, -
## trong trc ngoai sau
