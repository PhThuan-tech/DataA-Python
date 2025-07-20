# cai dat numpy thi o phan package : tim numpy r install la dc

import numpy as np

# tao 1 mang su dung numpy
A = np.array([1,2,3,4])
print(A)

# ngoai ra con co cac ham hay gap
"""
ones  : tao 1 mang full 1
zeros : tao 1 mang full 0
arange : tao 1 mang theo dieu kien (vi du: day chan tu 0 ->10)
"""

A1 = np.zeros((3,4))
print(A1)
A2 = np.ones((3,3))
print(A2)
A3 = np.arange(0,10,2)
print(A3)

# truy cap vi tri cua Array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0,1])
print(A[1:4])

#indice su dung array de de truy cap phan tu cua array khac
B1 = np.array([10 ,20, 30, 40, 50, 60])
id = np.array([1,3,5])     # dung mang de truy cap phan tu cua mang khac
print(B1[id])

# basic operator
C = np.array([3,4,5,6])
D = np.array([2,2,1,3])
operate = C + D     # + , -, *. /
print(operate)
# hoac dung cach khac / Binary operate
sumA = np.add(C,D)
print(sumA)

positive = np.array([-1,-2,-10,0,2,10])
print(abs(positive))

# ngoai ra con ham luong giac


