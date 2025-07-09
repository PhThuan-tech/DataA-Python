#List trong Python : dynamic array
# tao ra danh sach
a = [0]
print(a * 10)

# cac thao tac append, extend, insert()
a = []
a.append(10)
print(a)

a.insert(0,5)
print(a)

a.extend([15, 20, 25])
print(a)

# update value trong list
a[1] = 100  # gan gia tri phan tu thu 2
print(a)

# remove element
## remove(<value.) : xoa gia tri trong list
a.remove(15)
print(a)

## pop() : xoa phan tu dau hoac cuoi
print("Popped element:", a.pop(0))
print("List sau khi xoa:", a)

### del xoa phan tu
del a[0]
print("sau khi xoa [0]:", a)
