from abc import ABC,abstractmethod

class Perimeter(ABC):
    @abstractmethod
    def cal_circle(self):
        pass
    def cal_square(self):
        pass
    def cal_rect(self):
        pass

class Circle(Perimeter):
    def cal_circle(self):
        print("Circle")
    def cal_square(self):
        pass
    def cal_rect(self):
        pass

class Square(Perimeter):
    def cal_circle(self):
        pass
    def cal_square(self):
        print("Square")
    def cal_rect(self):
        pass

class Rectangle(Perimeter):
    def cal_circle(self):
        pass
    def cal_square(self):
        pass
    def cal_rect(self):
        print("Rectangle")

obj = Circle()
obj.cal_circle()




