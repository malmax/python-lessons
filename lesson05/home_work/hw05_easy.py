# -*- coding: utf-8 -*-
"""Малахов Максим."""
import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой
#  запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def createdirs():
    """Создание папок."""
    currentDir = os.path.dirname(__file__)
    for i in range(1, 10):
        try:
            dirName = "dir_" + str(i)
            os.mkdir(os.path.join(currentDir, dirName))
        except:
            print("Папка {} уже существует".format(dirName))


def deletedirs():
    """Удаление папок."""
    currentDir = os.path.dirname(__file__)
    for i in range(1, 10):
        try:
            dirName = "dir_" + str(i)
            os.rmdir(os.path.join(currentDir, dirName))
        except:
            print("Папка {} не существует".format(dirName))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def showdir():
    """Отображает содержимое папки."""
    currentDir = os.path.dirname(__file__)
    for dirName in os.listdir(currentDir):
        if os.path.isdir(os.path.join(currentDir, dirName)):
            print(dirName)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copyself():
    """Копирование текущего файла."""
    with open(__file__, "r") as f:
        txt = f.read()
    with open(__file__ + "copy", "w") as f:
        f.write(txt)
