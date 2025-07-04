#Tuple : gan giong list nhung dc: ordered , heterogeneous and immutable.

#Tao Tuple : duoc tao trog ( )
tup = ()
print(tup)

##Su dung tup kieu du lieu String
tup = ('hello', 'word', 10)
print(tup)

##Bien list thanh tuple
list1 = [1, 2, 3, 4, 5]
print(tuple(list1))

## Built-in Func
print(tuple('Thuan'))

## 2 tuple trong 1
tup1 = ('cam')
tup2 = ('da')
tup3 = (tup1, tup2)
print(tup3)

## SU DUNG OPERATOR
tup4 = ('taos',) * 3
print(tup4)

# truy cap trong Tuple
tup1 = tuple("abcdeftg")
print(tup1[1])          #in vi tri i
print(tup1[1:4])         #in theo slice
print(tup1[:5])

# unpack value tup1
tup =("command", "solad", "kiwi")
a, b, c = tup
print(a)
print(b)
print(c)

#cac thao tac voi trong tuple
tup = tuple("coworkerline")
print(tup[1:])
print(tup[::-1])
print(tup[4:9])
