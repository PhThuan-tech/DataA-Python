#String , List va tuplit
from traceback import print_tb

#nhap xau nhieu dong tro nen thi dung """ or '''
stt = """Hello I'm Thuan
And i'm learning Python"""

print(stt)

#truy cap vi tri cua xau
print("Xau stt vi tri 0 la :",stt[0])
## ngoai ra con co chi so i - stt.len : cach goi khac
print("Xau stt vi tri -13 la :", stt[-13])

# lay xau con s[i:j] lay tu i -> j
print(stt[0:10])
print(stt[:3])  # in tu dau den 2
print(stt[1:])  # in tu 1 den cuoi
print(stt[::-1]) # dao nguoc xau

# String la 1 dai lung bat bien (immutable)
## nen su dung cac pp chen, cat, dinh danh de fix thay vi gan stt[i]
s = "Improve"
s = s + "s and " + s ## do phai tao lai xau moi
print(s)

# updating a string
s = "hello Thuan"
s1 = "H" + s[1:]
s2 = s.replace("Thuan", "Vuong Thuan")
print(s1)
print(s2)

#upper va lower
str1 = "hello word"
print(str1.upper())
print(str1.lower())

#strip(): xoa khoang trang o 2 ben va replace(): thay the
str2 = "     Thuan dep trai      "
print(str2.strip())

# Operator trong python + va *
print("hello " * 3)
print("hello" + " word")

# string format o bai truoc
# kiem tra xau con co ton tai trong xau me ko
str3 = "Xin chao nguoi ban cua toi"
print("cua" in str3)
print("helo" in str3)
