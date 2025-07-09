# numpy hoac array cua python co san
# hoac dung list cx dc =))
import array as arr

from CoBan.CoBan8 import count

# .arr(data_type, value_list) - i, d, b, s
a = arr.array('i',[1,2,3,5,5,7,8,9,0,1,2,3,4])
print(a[2])

# insert(index, value)
a.insert(3, 4)
print(a)       # in ra la :array('i', [1, 2, 3, 4])
print(*a)      # in ra 1 2 3 4

# .append(value)
a.append(5)
print(*a)

# . remove(), .pop() tuong tu mau DS khac

# slice array
sliceArrayed = a[2 : 4]
print(sliceArrayed)

# tim index trong 1 array
print(a.index(3))

# count(value) : dem so phan tu co gia tri trong array
count = a.count(5)
print(count)

# .revese()
a.reverse()
print(a)

# .extend()
a.extend([0, 0, 0, 0])
print(a)