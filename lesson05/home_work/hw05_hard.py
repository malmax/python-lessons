# -*- coding: utf-8 -*-
"""Малахов Максим."""
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) - в Linux начинается с /, в Windows
# с имени диска
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы
# находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
# print('sys.argv = ', sys.argv)


def print_help(null):
    """Вывод доступных команд."""
    print("help - получение справки")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def copy_file(path):
    """Копируем указанный файл."""
    if os.path.isfile(path):
        basename = os.path.basename(path)
        try:
            with open(path, "r") as f:
                txt = f.read()
            with open(path + ".copy", "w") as f:
                f.write(txt)
            print("Удачно скопировали файл {}".format(basename))
        except Exception as e:
            print("Не удалось скопировать {}".format(basename))
            print(str(e))


def remove_file(path):
    """Удаляет указанный файл."""
    basename = os.path.basename(path)
    if os.path.isfile(path):
        confirm = input("Удалить файл {}? (Y/n)".format(basename))
        if confirm != "Y":
            return
        try:
            os.remove(path)
            print("Удалили файл {}".format(basename))
        except Exception as e:
            print("Не удалось удалить {}".format(basename))
            print(str(e))


def change_dir(path):
    """Меняем директорию."""
    try:
        if os.path.isdir(path):
            os.chroot(path)
            print("Удачно перешли в папку {}".format(path))
        else:
            print("Невозможно перейти в папку {}".format(path))
    except Exception as e:
        print("Невозможно перейти в папку {}".format(path))
        print(str(e))


def show_path(null):
    """Показывает полный путь директории."""
    print(os.getcwd())


do = {
    "help": print_help,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": show_path
}

try:
    second_arg = sys.argv[2]
except IndexError:
    second_arg = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key](second_arg)
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
else:
    print_help()
