#that ra da hinh von di da gap qua nhieu
# vi du max cua so nguyen ( da hinh la so thuc,string,..)
# ten ham trong 2 lop trung ten -> da hinh

# vi du ve 2 lop ke thua( lop cha co 1 ham - lop con cung co 1 ham giong ten)
class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # dinh nghia lai ham tinh area
    def area(self):
        return self.width * self.length

## tuong tu circle cung giong nhu tren

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# tao doi tuong ( neu nhieu doi tuong thi dung list)
shapes = [Rectangle(2,3), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")

