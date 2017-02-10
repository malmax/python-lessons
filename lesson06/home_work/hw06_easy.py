# -*- coding: utf-8 -*-
"""Малахов Максим."""
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех
# точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
import random


class Vector:
    """Определение координат."""

    def __init__(self, x, y):
        """Конструктор."""
        self.x = x
        self.y = y

    def __sub__(self, vector2):
        """Вычитание координат. Возвращаем длину."""
        x = (self.x - vector2.x)
        y = (self.y - vector2.y)
        return Vector(x, y)

    def __mul__(self, vector2):
        """Скалярное перемножение векторов."""
        return self.x * vector2.x + self.y * vector2.y

    @property
    def len(self):
        """Длина вектора."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        """Вывод в строку."""
        return "({}, {})".format(self.x, self.y)

    def get_angle_between(self, vector2):
        """Вычисляем угол между текущим вектором и vector2."""
        cosA = self * vector2 / (self.len * vector2.len)
        return math.acos(cosA)


class Triangle:
    """Треугольник."""

    def __init__(self, a, b, c):
        """Конструктор."""
        if(isinstance(a, Vector)):
            self.a = a
        else:
            raise
        if(isinstance(b, Vector)):
            self.b = b
        else:
            raise
        if(isinstance(c, Vector)):
            self.c = c
        else:
            raise

    def get_perimetr(self):
        """Периметр."""
        ab = self.a - self.b
        # print("ab: ", str(ab))
        bc = self.b - self.c
        # print("bc: ", str(bc))
        ca = self.c - self.a
        # print("ca: ", str(ca))

        return (ab.len + bc.len + ca.len)

    def get_square(self):
        """Вычисляем площадь по формуле 1/2·a·b·sin(γ)."""
        ab = self.a - self.b
        ca = self.c - self.a
        angle = ab.get_angle_between(ca)
        return 0.5 * ab.len * ca.len * math.sin(angle)

    def __str__(self):
        """Вывод в строчку."""
        return "a: {}, b: {}, c: {}".format(self.a, self.b, self.c)


triangle = Triangle(
            Vector(random.randint(-10, 10), random.randint(-10, 10)),
            Vector(random.randint(-10, 10), random.randint(-10, 10)),
            Vector(random.randint(-10, 10), random.randint(-10, 10)))
print(str(triangle))
print(triangle.get_perimetr())
print(triangle.get_square())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х
# точек. Предусмотреть в классе методы: проверка, является ли фигура
# равнобочной трапецией; вычисления: длины сторон, периметр, площадь.


class Trapecia:
    """Равнобочная трапеция."""

    def __init__(self, a, b, c, d):
        """Конструктор."""
        if(isinstance(a, Vector)):
            self.a = a
        else:
            raise
        if(isinstance(b, Vector)):
            self.b = b
        else:
            raise
        if(isinstance(c, Vector)):
            self.c = c
        else:
            raise
        if(isinstance(d, Vector)):
            self.d = d
        else:
            raise

        self.ab = self.a - self.b
        self.bc = self.b - self.c
        self.cd = self.c - self.d
        self.da = self.d - self.a

    def is_trapecoid(self):
        """True если равнобочная трапеция."""
        # Если одинаковые стороны ab и cd
        if self.ab.len == self.cd.len and self.bc.len != self.da.len:
            if self.bc.len > self.da.len:
                self.squareAngle = (self.c - self.b).get_angle_between(self.ab)
                self.squareC = self.ab.len
                self.squareA = self.bc.len
            else:
                self.squareAngle = (self.da).get_angle_between(self.b - self.a)
                self.squareC = self.ab.len
                self.squareA = self.da.len

            return True

        if self.bc.len == self.da.len and self.ab.len != self.cd.len:
            if self.ab.len > self.cd.len:
                self.squareAngle = (self.c - self.b).get_angle_between(self.ab)
                self.squareC = self.bc.len
                self.squareA = self.ab.len
            else:
                self.squareAngle = (self.a - self.d).get_angle_between(self.cd)
                self.squareC = self.bc.len
                self.squareA = self.cd.len

            return True

    def get_perimetr(self):
        """Получение периметра трапеции."""
        return self.ab.len + self.cd.len + self.bc.len + self.da.len

    def get_square(self):
        """Вычисление площади через стороны и угол."""
        # http://www-formula.ru/index.php/2011-09-19-02-39-24/trapeze-area
        if self.is_trapecoid():
            return self.squareC * math.sin(self.squareAngle) * (self.squareA -
             self.squareC * math.cos(self.squareAngle))


trapecioid = Trapecia(Vector(0, 0), Vector(1, 5), Vector(9, 5), Vector(10, 0))
print(trapecioid.is_trapecoid())
print(trapecioid.get_perimetr())
print(trapecioid.get_square())
