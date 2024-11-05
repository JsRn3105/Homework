import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = int(input("Введите сторону квадрата: "))
area_of_square = square(side_length)

print(f"Площадь квадрата: {area_of_square}")
