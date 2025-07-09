"""
comment tao nhu the nay
"""

""" tao 1 mang 1 chieu"""
a = [1, 2, 3, 4, 10]
b = [-10, 0.1, 21, "love"]
print('danh sach mang:', a)
print('danh sach phan tu trong b:', b)

print("in ra phan tu tai index 0: ",a[0]); print(a[1]); print(a[4])

print('in ra danh sach tu 0 toi 3: ', a[0 : 3])

# comment cach thu 2 (them nhieu ##### cx ko sao)
print('chuoi co chua # van la xau')

# dang bool
condition = (10 < 11) and (11 < 20 > 10)
print('Dieu kien cua boolean:', condition)

# su dung in va not in
a1 = 1
b1 = 10
a2 = [0 , 20, 30, 30, 1]
print('kiem tra a1 co trong a2 :', a1 in a2)
print('kiem tra b1 co trong a2 :', b1 not in a2)

b = [
    [1, 2, 3],
    [0, 2, 1],
    [1, 1, 0]
]
print(b)
