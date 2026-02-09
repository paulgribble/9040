# procedural way:
circle1 = {"type":"circle", "radius":3.0, "name":"pepperoni"}
circle2 = {"type":"circle", "radius":5.0, "name":"tomato"}
square1 = {"type":"square", "side": 10.0, "name":"pizzabox"}

def computeAreaOfCircle(circle):
    return circle["radius"]**2 * 3.14159

def computeAreaOfSquare(square):
    return square["side"]**2

def computeArea(shape):
    if (shape["type"] == "circle"):
        return shape["radius"]**2 * 3.14159
    elif (shape["type"] == "square"):
        return shape["side"]**2

# The OOP way

class Circle():
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
    def __repr__(self):
        return f"I am a circle called {self.name} with radius {self.radius}"
    def __lt__(self, other):
        return (self.computeArea() < other.computeArea())
    def __gt__(self, other):
        return (self.computeArea() > other.computeArea())
    def __eq__(self, other):
        return (self.computeArea() == other.computeArea())
    def computeArea(self):
        return self.radius**2 * 3.14159

class Square():
    def __init__(self, name, side):
        self.name = name
        self.side = side
    def __repr__(self):
        return f"I am a square called {self.name} with side {self.side}"
    def __lt__(self, other):
        return (self.computeArea() < other.computeArea())
    def __gt__(self, other):
        return (self.computeArea() > other.computeArea())
    def __eq__(self, other):
        return (self.computeArea() == other.computeArea())
    def computeArea(self):
        return self.side**2

circle1 = Circle(name="pepperoni", radius=3.0)
circle2 = Circle(name="tomato", radius=5.0)
square1 = Square(name="pizzabox", side=12.0)
square2 = Square(name="table",side=100)
