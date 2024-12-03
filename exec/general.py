#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
В некой игре-стратегии есть солдаты и герои. У всех
есть свойство, содержащее уникальный номер объекта, и свойство, в котором
хранится принадлежность команде. У солдат есть метод «иду за героем»,
который в качестве аргумента принимает объект типа «герой». У героев есть
метод увеличения собственного уровня.
В основной ветке программы создаётся по одному герою для каждой
команды. В цикле генерируются объекты-солдаты. Их принадлежность
команде определяется случайно. Солдаты разных команд добавляются в
разные списки.
Измеряется длина списков солдат противоборствующих команд и
выводится на экран. У героя, принадлежащего команде с более длинным
списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите
на экран идентификационные номера этих двух юнитов.

Выполнил студент группы ИВТ-б-о-22-1
'''

import abc
import random


class Unit:

    @abc.abstractmethod
    def __init__(self, id, commaind_id):
        '''Метод инициализации'''
        pass

    @abc.abstractmethod
    def action(self, *args):
        '''Метод действия'''
        pass


class Solder(Unit):

    def __init__(self, id, command_id):
        '''Метод инициализации солдата'''
        self.id = id
        self.command_id = command_id

    def action(self, hero):
        '''Метод действия солдата'''
        if isinstance(hero, Hero):
            print("Солдат: Следую за Героем!")
        else:
            TypeError


class Hero(Unit):

    def __init__(self, id, command_id):
        '''Метод инициализации героя'''
        self.id = id
        self.command_id = command_id
        self.level = 1

    def action(self):
        '''Метод действия героя'''
        self.level += 1
        print(f"Уровень Героя {self.id} повышен до уровня {self.level}!")


if __name__ == '__main__':
    '''Основной метод'''
    hero1 = Hero(1, 0)  # Создание героя 1
    hero2 = Hero(2, 1)  # Создание героя 2

    # Создание список для распределения солдат
    firstTeamUnitList = []
    secondTeamUnitList = []

    # Цикл для распределения солдат по командам
    for i in range(30):
        team = random.randint(0, 1)
        if team == 0:
            firstTeamUnitList.append(Solder(i + 3, 0))
        else:
            secondTeamUnitList.append(Solder(i + 3, 1))

    firstCount = firstTeamUnitList.__len__()
    secondCount = secondTeamUnitList.__len__()

    # Сравнение количества солдат в каждой команде
    if firstCount > secondCount:
        hero1.action()
    elif secondCount > firstCount:
        hero2.action()
    else:
        print("Результат битвы: Ничья")

    # Вывод детальной информации по командам
    print("-----" * 4, "[Команда 1]", "-----" * 4)
    print(f"Уровень героя: {hero1.level}")
    print(f"Количество юнитов в команде: {firstTeamUnitList.__len__()}\n")
    print("-----" * 4, "[Команда 2]", "-----" * 4)
    print(f"Уровень героя: {hero2.level}")
    print(f"Количество юнитов в команде: {secondTeamUnitList.__len__()}\n")

    randomSolder = firstTeamUnitList[random.randint(0, firstCount - 1)]
    randomSolder.action(hero1)
    print(f"ID Героя 1: {hero1.id}")
    print("ID случайного солдата Героя 1: "
          f"{randomSolder.id}")
