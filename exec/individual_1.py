#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Pair:

    def __init__(self, x, y):
        '''Инициализация объекта с указанием двух значений переменных'''
        self.x = x
        self.y = y

    def set_values(self, x, y):
        '''Установка значений переменных x и y отдельным методом'''
        self.x = x
        self.y = y

    def mul(self):
        '''Возвращает произведение значений переменных x и y'''
        return self.x * self.y


class RightAngled(Pair):

    def __init__(self, cath1, cath2):
        '''Инициализация с наследованием от класса Pair'''
        super().__init__(cath1, cath2)

    def hypotenuse(self):
        '''Вычисление гипотенузы по заданным катетам
        Значения x и y не объявлялись, т.к. наследованы от класса Pair'''
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def square(self):
        '''Вычисление площади треугольника по катетам
        Значения x и y не объявлялись, т.к. наследованы от класса Pair'''
        return (self.x * self.y) / 2


if __name__ == "__main__":
    # Основной метод программы
    pair = Pair(0, 0)  # Создание нового объекта класса Pair
    pair.set_values(5, 10)  # Отдельная установка значений x и y
    # Вывод значений x и y, вычисление произведения
    print(f"Произведения чисел {pair.x} и {pair.y} равно {pair.mul()}")

    triangle = RightAngled(4, 12)  # Создание нового объекта класса RightAngled
    # Определение гипотенузы треугольника с поомщью метода hypotenuse по
    # установленным в предыдущей строке значениям, вывод этих значений и
    # результата расчёта.
    print(f"\nГипотенуза треугоника с катетами {triangle.x} и"
          f" {triangle.y} равна {round(triangle.hypotenuse(), 4)}")
    # Определение площади треугольника с помощью метода square
    print(f"Площадь треугольника равна {triangle.square()}")
