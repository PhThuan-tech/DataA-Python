# tao 1 dictionary nhu sau {key : value} - theo kieu so nguyen
from os import remove

dct = {1 : 'Thuan', 2 : 'Vuo' , (1, 3) : [12 , 4, 0]}
print(dct)


# su dung theo thu vien dict() - dung cho kieu string
d1 = dict(name = "Thuan", animal = "money")
## d1 = dict(name = "hello", animal = "world")
print(d1)

# truy cap phan tu trong dict
print(d1["name"])       #in ra phan tu co key = name

## cach khac dung .get()
ans = d1.get("animal")
print(ans)

ans1 = dct.get((1, 3))
print(ans1)

# cac thao tac removing
a1 = {-10 : 'dog', 0 : 'cat', 1 : 'bird', (2,5) : 'T-rex'}

## del : xoa theo dia chi cua key
del a1[-10]
print(a1)

## pop : xoa theo dia chi cua key + xuat ra phan tu do
res1 = a1.pop(0)
print(res1)
print(a1)

## popitem : xoa phan tu do roi in theo key-value cua phan tu cuoi
key, val = a1.popitem()
print(f"key la: {key} va Value la: {val}")

## clear() : xoa all item
b1 = {1 : "abc", 2 : "bca", 3 : "dav"}
b1.clear()
print(b1)

# thao tac them :( giong database)
b1["control"] = 12312
b1['super idol'] = 2021
print(b1)

## su dung vong lap
a1 = {'cart1' : 1, 'vehicle' : 2, 'donkey' : 15}
for a in a1:            # in ra key
    print(a)

for a in a1.values():   # in ra value
    print(a)

# in ra ca key:value thi sao ?
for a,b in a1.items():
    print(f"key: {a} - value: {b}")