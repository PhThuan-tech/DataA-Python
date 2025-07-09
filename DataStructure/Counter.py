# cac bai sau thi su dung thu vien collections
from collections import Counter

res = Counter([1, 2, 3, 4, 2, 1, 3, 4, 4, 4, 1, 1])
print(res)      # 1 xuat hien 4 lan, 4 : 4, 2 :2 , 3 : 2
# in ra so xuat hien nhieu nhat r giam dan den thap nhat

res1 = Counter('Helloeliot')
print(res1)

# truy cap so lg phan cua 1 phan tu (neu ton tai)
print(res[1])

# cap nhat counter (update) phan tu - them vao
ctr = Counter([1,2,3])
ctr.update([4,5,2,1])       # -> [1,2,3,4,5,2,1]
print(ctr)

# gio chuyen nguoc tu Counter -> List: su dung ep kieu va truy cap elements cua counter
res2 = list(ctr.elements())
print(res2)     # no se dc sap xep tang dan

# .subtract()   # tru di cac phan tu trong Counter ( -1 dv, neu ko co la so am)
ctr.subtract([5,2,1])
print(ctr)

# co the su dung cac phep toan "+", "-", "&"(giao) va "|"(hop)




