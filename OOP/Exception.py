# vi du ve xu li ngoai le
n = 10
try:
    res = n / 0

except ZeroDivisionError:
    print("Ko the chia cho 0")

""" cau truc cua xu li ngoai le
try:
    # code co the gay ra loi
except <Loai Loi hay gap>:
    # xu li loi
else:
    # chay doan nay neu ko loi
finally:
    # code luon thuc thi(dung hay sai)
"""

try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")

## co the xu li nhieu loai ngoai le khac nhau
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int

except (ValueError, TypeError) as e:
    print("Error", e)

except IndexError:
    print("Index out of range.")

# 1 so loi hay gap
# https://www.geeksforgeeks.org/python/built-exceptions-python/

#dinh nghia 1 ngoai le rieng
# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 3: Handling the custom exception
try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)