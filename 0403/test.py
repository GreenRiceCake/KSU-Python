def emp():
    pass

def msg():
    print("Hello World")
    print("Welcome to Python programming")
    print("This is a test message")

def msg2(rep):
    for i in range(rep):
        print("This is a repeated message")

def getArea(radius):
    area = 3.14 * radius ** 2
    return area
emp()
msg()
msg2(3)
area = getArea(5)
print("The area of the circle with radius 5 is:", area)