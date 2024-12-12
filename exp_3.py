from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self):
        self.length = 0
        self.width = 0

    def get_dimensions(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        area = self.length * self.width
        return area

class Triangle(Polygon):
    def __init__(self):
        self.base = 0
        self.height = 0

    def get_dimensions(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        return area

if __name__ == "__main__":
    print("Choose a polygon to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        rectangle = Rectangle()
        rectangle.get_dimensions()
        area = rectangle.calculate_area()
        print(f"The area of the rectangle is: {area}")

    elif choice == "2":
        triangle = Triangle()
        triangle.get_dimensions()
        area = triangle.calculate_area()
        print(f"The area of the triangle is: {area}")

    else:
        print("Invalid choice. Please select either 1 or 2.")

