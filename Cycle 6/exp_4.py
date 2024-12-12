class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        """Method to calculate the area of the rectangle."""
        return self.length * self.breadth

    def perimeter(self):
        """Method to calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.breadth)


if __name__ == "__main__":
    print("Enter the dimensions for Rectangle 1:")
    length1 = float(input("Enter the length of the rectangle: "))
    breadth1 = float(input("Enter the breadth of the rectangle: "))
    rect1 = Rectangle(length1, breadth1)
    print("\nEnter the dimensions for Rectangle 2:")
    length2 = float(input("Enter the length of the rectangle: "))
    breadth2 = float(input("Enter the breadth of the rectangle: "))
    rect2 = Rectangle(length2, breadth2)
    print(f"\nRectangle 1 - Area: {rect1.area()} | Perimeter: {rect1.perimeter()}")
    print(f"Rectangle 2 - Area: {rect2.area()} | Perimeter: {rect2.perimeter()}")
    area1 = rect1.area()
    area2 = rect2.area()

    if area1 < area2:
        print("\nRectangle 1 has a smaller area than Rectangle 2.")
    elif area1 == area2:
        print("\nRectangle 1 and Rectangle 2 have the same area.")
    else:
        print("\nRectangle 1 has a larger area than Rectangle 2.")

