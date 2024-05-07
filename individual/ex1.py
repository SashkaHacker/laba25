#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Вариант 10
# Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
# имеющиеся в Python средства перегрузки операторов.
# Условие индивидуального задания 1 лабораторной работы № 4.1: 
# Линейное уравнение y = Ax + B. Поле first — дробное число, коэффициент A; поле second
# — дробное число, коэффициент B. Реализовать метод function() — вычисление для
# заданного x значения функции y.


class LinearEquation:
    def __init__(self, first, second):
        if not isinstance(first, (int, float)) or not isinstance(
            second, (int, float)
        ):
            raise ValueError("Коэффициенты должны быть числами.")
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите коэффициент a: "))
        self.second = float(input("Введите коэффициент b: "))

    # Заменил метод display на __repr__
    def __repr__(self):
        return f"Линейное уравнение: {self.first}x + {self.second} = 0"

    # Заменил метод function на __call__
    def __call__(self, x):
        return self.first * x + self.second


if __name__ == "__main__":
    equation1 = LinearEquation(1, 2)
    print(equation1)
    print(equation1(10))

    equation2 = LinearEquation(0, 0)
    equation2.read()
    print(equation2)
    x = float(input("Введите значение x для вычисления функции: "))
    print(f"Значение функции: {equation2(x)}")
