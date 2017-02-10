# -*- coding: utf-8 -*-
"""Малахов Максим."""
import sys
import os

# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками
# текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"


def printHelp():
    """Выводим хэлп."""
    # print("{}".format(os.path.dirname()))
    print("""
        1. Перейти в папку
        2. Просмотреть содержимое текущей папки
        3. Удалить папку
        4. Создать папку
        5. Выход
        """)


while True:
    currentDir = os.getcwd()
    print("Текущая папка:", currentDir)
    printHelp()
    key = input("Введите команду: ")

    if key == '1':
        dirName = input("Введите название папки: ")
        try:
            toDir = os.path.join(currentDir, dirName)
            if os.path.isdir(toDir):
                os.chdir(toDir)
                print("Удачно перешли в папку {}".format(dirName))
            else:
                print("Невозможно перейти в папку {}".format(toDir))
        except Exception as e:
            print("Невозможно перейти в папку {}".format(dirName))
            print(str(e))
    elif key == '2':
        for dirName in os.listdir(currentDir):
            if os.path.isdir(os.path.join(currentDir, dirName)):
                dirType = "Папка"
            else:
                dirType = "Файл"
            print("{} - {}".format(dirType, dirName))
    elif key == '3':
        dirName = input("Введите название папки для удаления: ")
        try:
            toDir = os.path.join(currentDir, dirName)
            confirm = input("Удалить папку {}? (Y/n)".format(toDir))
            if os.path.isdir(toDir) and confirm == 'Y':
                os.rmdir(toDir)
                print("Удачно удалили папку {}".format(dirName))
            else:
                print("Невозможно удалить папку {}".format(toDir))
        except Exception as e:
            print("Невозможно удалить папку {}".format(dirName))
            print(str(e))
    elif key == '4':
        dirName = input("Введите название папки для создания: ")
        try:
            toDir = os.path.join(currentDir, dirName)
            os.mkdir(toDir)
            print("Удачно создали папку {}".format(dirName))
        except Exception as e:
            print("Невозможно создать папку {}".format(dirName))
            print(str(e))
    else:
        sys.exit()

    input("Нажмите любую кнопку, чтобы продолжить...")
    # print(chr(27) + "[2J")


# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл
# из easy.py

import hw05_normal as normal

normal.createdirs()
normal.deletedirs
