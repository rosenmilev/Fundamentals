class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.r = diameter / 2

    def calculate_circumference(self):
        return self.r * 2 * Circle.__pi

    def calculate_area(self):
        return Circle.__pi * (self.r ** 2)

    def calculate_area_of_sector(self, angle):
        return angle / 360 * Circle.__pi * (self.r ** 2)

    def test(self):
        self.__pi += 1
        return self.__pi


test = Circle(11)

print(test.test())