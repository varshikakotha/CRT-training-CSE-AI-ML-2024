# an abstract class contains abstract methods where they are not having body,body is presented in inheriting classes(child classes)

from abc import ABC , abstractmethod

class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_circle_area(self):
        pass

class Square():
    def calculate_area(self):
        print("in square method")
    def

class Rectangle():
    pass

ob  = Square()
ob.calculate_area()
