# -*- coding: utf-8 -*-
"""Малахов Максим."""
import os
print('os.name = ', os.name)
print('os.environ = ', os.environ)
print('os.getcwd() = ', os.getcwd())

files = os.listdir(os.getcwd())
print(files)

print("current dir = ", os.path.dirname(__file__))

# Создаем новую директорию
dir_path = os.path.join(os.getcwd(), 'NewDir')
print(dir_path)
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует')
