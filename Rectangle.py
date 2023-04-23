"""
Добавил проверку (строки 23 - 29):
    def validate(self, value): # Проверка введеных значений на число и отрицательное число.
        if type(value) == int or type(value) == float:
            if value < 0:
                raise Exception(f"Значение не должно быть отрицательным: {value}")
        else:
            raise Exception(f"Введено не число: {value}")
        return value
"""
class Rectangle:

    def __init__(self, width, height: None = None):
        self.width = Rectangle.validate(self, width)
        self.height = Rectangle.validate(self, height or width)

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_area(self) -> float:
        return self.width * self.height

    def validate(self, value): # Проверка введеных значений на число и отрицательное число.
        if type(value) == int or type(value) == float:
            if value < 0:
                raise Exception(f"Значение не должно быть отрицательным: {value}")
        else:
            raise Exception(f"Введено не число: {value}")
        return value


if __name__ == '__main__':
    rect = Rectangle(10.5, "five")
    print(rect.get_perimeter())
    print(rect.get_area())

    square = Rectangle(10)
    print(square.get_perimeter())
    print(square.get_area())