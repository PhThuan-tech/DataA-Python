age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# toan tu 3 ngoi
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

#switch case
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

# vong lap whie - while else va for in range
count = 0
while count < 3 :
    print(count)
    count = count + 1
else:
    print("Ket thuc vong lap while")    # khi dieu kien while sai thi chay

## vong lap for
for i in range(10):
    print(i, end=" ")   #dung de in theo hang ngang thay vi xuong dong

print("\n")             # xuong dong
for j in range(4,6):
    print(j * 2, end=" ")

print("")
lis = ["toi", "ten", "la", "thuan"]
for item in lis:        # dung chi so index la: range(len(list)):
    print(item, end=" ")
print("\n")

string1 = "hello word"
for s in string1:
    print(s, end=" ")
print("\n")

## ngoia ra con dung cho tuple, dictionary, set, map,..

## vong lap chong nhau
for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

## su dung duoc ca break va continue trong python
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

