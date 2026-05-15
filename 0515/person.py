class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age

p = Student("gildong", 27)
print(p.getAge())
print(p.getName())
p.setAge(20)
p.setName("donghwi")
print(p.getName(), p.getAge())
s = Student()
print(s.getName(), s.getAge())

