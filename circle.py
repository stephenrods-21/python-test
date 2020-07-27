from math import pi


class Circle:

    def __init__(self, radius=1.0):
        self.radius = radius

    def __str__(self):
        return 'Circle with radius of {:.2f}'.format(self.radius)

    def get_area(self):
        return 'Area of circle with radius {0} is {1:.2f}'.format(self.radius, self.radius ** 2 * pi)

    def get_perimeter(self):
        return 'Perimeter of circle with radius {0} is {1:.2f}'.format(self.radius, pi * (2 * self.radius))


if __name__ == '__main__':
    radius = int(input('Enter the radius\n'))
    circle_a = Circle(radius)
    print(circle_a.get_area())
    print(circle_a.get_perimeter())
