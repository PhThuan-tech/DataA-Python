#Set() : sap xep theo thu tu tang dan, ko trung phan tu
set1 = {3,0,4,5,5,0,3}    #loai bo cac phan tu bi trung
print(set1)

# ko truy cap dc phan tu theo chi so
##xu li ngoai le: try - except
try:
    print(set1[0])
except TypeError as e:
    print(e)

# them phan tu va xoa phan tu
set1.add(2)     # them 1 phan tu
set1.update([1, 6, 7]) # them nhieu phan tu
print(set1)

a1 = set1.pop()    # xoa phan tu dau tien va in ra man hinh
print(a1)

set1.remove(7)
print(set1)

set1.clear()
print(set1)     # se in ra set()

# truy cap phan tu su dung vong lap
set2 = {5, 4, 3, 2, 1, 0}
for i in set2:
    print(i, end=" ")

print("hello" in set2)

# frozenSet: giong set nma ko thay doi duoc giong hang so

fset1 = frozenset([1,2,3,4,5,6])
print(fset1)

## cach khac
set3 = {3, 4, 5, 6,7 ,8 ,9}
fset2 = frozenset(set3)
print(fset2)

# chuyen doi tuong(DS -> set)
string1 = "HelloEveryOne"
sets = set(string1)
print(sets)
## dict -> set, list -> set,....