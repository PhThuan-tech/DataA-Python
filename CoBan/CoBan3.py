#Quy tac dat ten bien
"""
-Khong bat dau bang chu so
-Khong dung cac tu khoa trong thu vine : class, float, integer
-khong chua cac ki tu khac : $#%^&**(!#
"""

# Cac bien trong Python la dynamic Variable thay doi, gan kieu j cung dc
x = y = z = 100
print(x + y + z)

x,y,z = 0, "hi", 100
print(x,y,z)

# Co che casting int(), float(), str()
x = "109"
print(int(x));

# lay ra kieu data cua bien
y = 10.91
print(type(y))

# phan biet Local Var va Global Var
## cac bien o ngoai Ham la Global
## cac bien o trong Ham la Local
def sum(a,b) :
    total = a + b  ## day la local
    print(total)
    print("Finished Sum of two number")
sum(10,2)

a = "I am Global"
def pr():
    global a    # casting bien Global thanh dia phuong
    a = "I am Local"
    print(a)

pr()
print(a)

# tham chieu doi tuong
a = "Super"
b = a
print(b)    # ca a va b deu tham chieu toi 1 dia chi

## neu xoa a thi sa0 ?
del a
print(b)    ## thi b van tham chieu binh thuong

## neu b tham chieu toi 1 doi tuong khac thi doi tuong cu se bien mat
b = "control"
print(b)

# xu li trong xau
word = "I have an apple"
n = len(word)
print("Do dai xau vua nhap la: ", n)