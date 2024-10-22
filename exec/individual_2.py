#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc


class Pair:

    @abc.abstractmethod
    def __init__(self, x, y):
        '''Метод инициализации'''
        pass

    @abc.abstractmethod
    def set_values(self, x, y):
        '''Метод смены значений'''
        pass

    @abc.abstractmethod
    def sum(self, x, y):
        '''Метод суммирования'''
        pass

    @abc.abstractmethod
    def subtract(self, x, y):
        '''Метод вычитания'''
        pass

    @abc.abstractmethod
    def divide(self, x, y):
        '''Метод деления'''
        pass

    @abc.abstractmethod
    def multiply(self):
        '''Метод произведения'''
        pass

    @abc.abstractmethod
    def display(self):
        '''Метод вывода значений'''
        pass


class Complex(Pair):

    def __init__(self, real, imagine):
        '''Метод инициализации комплексных чисел'''
        self.real = real
        self.imagine = imagine

    def sum(self, other):
        '''Метод суммирования комплесных чисел'''
        return Complex(self.real + other.real, self.imagine + other.imagine)

    def subtract(self, other):
        '''Метод вычитания комплексных чисел'''
        return Complex(self.real - other.real, self.imagine - other.imagine)

    def multiply(self, other):
        '''Метод произведения комплексных чисел'''
        z1 = self.real * other.real - self.imagine - other.imagine
        z2 = self.real * other.imagine + self.imagine * other.real
        return Complex(z1, z2)

    def divide(self, other):
        '''Метод деления комплексных чисел'''
        z1 = self.real * other.real + self.imagine * other.imagine
        z2 = other.real ** 2 + other.imagine ** 2
        z3 = other.real * self.imagine - self.real * other.imagine
        return Complex(round(z1 / z2, 4), round(z3 / z2, 4))

    def display(self):
        '''Метод вывода комплексных чисел'''
        return f'{self.real} + {self.imagine}i'


class Rational:

    def __init__(self, x, y):
        '''Метод инициализации рационального числа'''
        self.x = x
        self.y = y

    def sum(self, other):
        '''Метод суммирования рациональных чисел'''
        if isinstance(other, Rational):
            return Rational(self.x * other.y + other.x * self.y,
                            self.y * other.y)

    def subtract(self, other):
        '''Метод вычитания рациональных чисел'''
        if isinstance(other, Rational):
            return Rational(self.x * other.y - other.x * self.y,
                            self.y * other.y)

    def multiply(self, other):
        '''Метод произведения рациональных чисел'''
        if isinstance(other, Rational):
            return Rational(self.x * other.x, self.y * other.y)

    def divide(self, other):
        '''Метод деления рационеальных чисел'''
        if isinstance(other, Rational):
            return Rational(self.x * other.y, other.x * self.y)

    def display(self):
        '''Метод вывода рационального числа'''
        return f'{self.x}/{self.y}'


if __name__ == "__main__":
    '''Основной методу'''

    print('-----[ Комплексные числа ]-----')
    c1 = Complex(5, 3)
    c2 = Complex(10, 2)
    print(f'Первое комплексное число: {c1.display()}')
    print(f'Второе комплексное число: {c2.display()}')
    print(f'z = ({c1.display()}) + ({c2.display()}) = {c1.sum(c2).display()}')
    print(f'z = ({c1.display()}) - ({c2.display()}) '
          f'= {c1.subtract(c2).display()}')
    print(f'z = ({c1.display()}) × ({c2.display()}) '
          f'= {c1.multiply(c2).display()}')
    print(f'z = ({c1.display()}) ÷ ({c2.display()}) '
          f'= {c1.divide(c2).display()}')

    print('\n-----[ Рациональные числа ]-----')
    r1 = Rational(4, 5)
    r2 = Rational(6, 9)
    print(f'{r1.display()} + {r2.display()} = {r1.sum(r2).display()}')
    print(f'{r1.display()} - {r2.display()} = {r1.subtract(r2).display()}')
    print(f'{r1.display()} × {r2.display()} = {r1.multiply(r2).display()}')
    print(f'{r1.display()} ÷ {r2.display()} = {r1.divide(r2).display()}')
