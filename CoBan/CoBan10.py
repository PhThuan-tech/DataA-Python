a = [1, 2, 3, 4]

for i in range(0,4):
    a[i] = a[i] *2
    print(a[i], end= " ")

print()
a1 = [1] * 5
print(a1)

# luyen tap string format
"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
"""
## thao tac voi string
data = ("Thuan", "K69A-AI1", 19)
# Nen dung tuple de chuyen sang string de hon, thay vi dung list

outputStr = "Hello My name is %s, I'm from class %s and %s years old!"% data
print(outputStr)

### thao tac voi float
nums1 = 21.1294
s = "Lam tron chu so thap phan 2 chu so: {:.2f}".format(nums1)
print(s)

## hoac dung cach nay
nums2 = 3.14357
s1 = "Lam tron so thap phan sau 2 chu so: %.2f" % nums2
print(s1)

##cac thao tac trong string - moi

str1 = "Good Afternoon"
print(str1.index('o'))  # chi in dc phan tu xuat hien dau tien
print(str1.count('t'))  # dem so phan tu xuat hien trong string
print(str1[4:9])        # cat xau con trong xau me
print(str1[1:10:2])     # start : end : step
print(str1[::-1])       # in xau dao nguoc
print(str1.upper() + " " + str1.lower())
print(str1.split(" "))  # Tach xau me thanh xau con

