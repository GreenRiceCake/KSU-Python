class Car:
    def __init__(self, speed, model, color):
        self.speed = speed
        self.model = model
        self.color = color
    def drive(self):
        self.speed = 60

c = Car(0, "Avante", "blue")
print(c.speed, c.model, c.color)
c.drive()
print("차량의 속도는 ", c.speed, "km/h 입니다.")