class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
      
my_rect = Rectangle(12, 6)

for item in my_rect:
    print(item)

