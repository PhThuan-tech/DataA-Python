#Function trong Python
def sayHello():         #Dinh nghia
     print("Good morning Mr/Mrs!")

sayHello()  # calling

## co tham so
def calculate(x: int, y: int):
    print("Sum:",x + y)
    print("Sub:",x - y)
    print("mul:",x * y)
    print("div:",x / y)
    print("mod:",x % y)

calculate(5,2)

## kiem tra so
def evenOdd(x):
    if(x % 2 == 0):
        return "Even"
    else:
        return "odd"

print(evenOdd(16))
print(evenOdd(5))

# Pos argu
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

#truyen tham so phai dung vi tri, ko la sai kieu tra ve
print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")    # do python mac dinh kieu du lieu ne ko pbiet dc

#tu khoa *args va *kwargs : dung de nhap kieu nhieu tham so + moi kieu data
## tu khoa *args
def fun(*args):
    return sum(args)

print(fun(1,2,100,-10,-1.51))

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

##tu khoa *kwargs : cho phép bạn truyền số lượng tham số không giới hạn dưới dạng key-value vào hàm.
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Thuận", age=20, mood="🔥")

## dung ca args ca kwargs :
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)

# Docstring: documentaion string - dung de mo ta chuc nag hanh dong cua phuong thuc khi goi
def evenOdd(x):
    """Function to check if the number is even or odd"""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

print(evenOdd.__doc__)  #mo ta cach hd cua func vua tao

#su dung lamda: la ham an danh = giong voi ham def bth nma ko co tu khoa def
# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))


# ham de quy : vi du tinh giai thua cua n
def factory(n):
    if n == 0:
        return 1
    else:
        return n * factory(n - 1)

print(factory(5))

#truyen tham chieu va truyen tham tri
def myType(list):       # truyen tham chieu trong 1 list
    list[0] = 10

list1 = [0, 1, 2, 3, 4, 5]
myType(list1)
print(list1)

## khi gan 1 gia tri trong 1 func thi se ko thay doi gia tri ma thay doi dia chi






