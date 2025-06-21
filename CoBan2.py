# nhap input va xuat ra input vua nhap
name = input("Enter your name: ")
yearold = input("Enter your age: ")
print("Hello,", name, "! Welcome!")
print("You are:", yearold, " old!")

# print nhieu loai bien da duoc gan
SurName = "Alice"
YearOld = 20
Hometown = "Bac Ninh"
print(SurName, YearOld, Hometown)

# Nhap Input nhieu (Dung split de ngan cach nhau boi 1 khoang trong
x,y = input("Enter two value: ").split()
print("Boy is: ", x)
print("Girl is: ", y)

# Xu li dieu kien - Take conditional
# chuyen doi input -> integer truoc(so sanh j thi chuyen ve kieu do)

age = int (yearold)

if age < 0 :
    print('What the hell?')
elif age < 18 :
    print("Nice bro")
elif age >= 18 and age < 65 :
    print("You are Adult")
else:
    print("You so old bro")

# Ep kieu cho input nhap vao tuy y
# Mac dinh input() nhap vao se la dang string

num = int(input('Nhap so nguyen :'))
# float(),boolean(),..
print(num)

#type cua Object dung nhu sau: type(Object)

# Output format
# sep='<char here>' : dung de ngan cach nhau boi 1 ki tu
print("My email is :phamthuan" ,"gmail.com",sep='@')
# su dung .format() kha la hay

# Su dung f-string
print(f"my name is: {name} and i'm {yearold}.")