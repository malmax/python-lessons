# -*- coding: utf-8 -*-
"""Малахов Максим."""
import os
from random import choice

BASE_DIR = "/home/malmax"


class Packer():
    """Реализация статичных методов и переменных."""

    counter = 0  # счетчик упаковок
    obj_count = 0

    def __init__(self, method, *files):
        """Конструктор."""
        Packer.obj_count += 1
        self._files = files

    def pack(self):
        """Упаковка файла."""
        Packer.counter += 1

    @classmethod
    def stat(cls):
        """Статичный метод."""
        print("Упаковок {}, всего объектов {}".format(cls.counter,
        cls.obj_count))
        return cls.counter, cls.obj_count

    @property
    def files(self):
        """Возвращаем все файлы."""
        files = [os.path.join(BASE_DIR, file) for file in self._files]
        return files

    @staticmethod
    def fast_pack(method, *files):
        for f in files:
            print("Packing {} with {}".format(f, method))

    @staticmethod
    def random_packer():
        m = choice(['zip', 'rar', 'gzip', 'bz2'])
        return Packer(m)


p1 = Packer("zip", "test1", "test2")
p2 = Packer("rar")
p3 = Packer("7z")

Packer.stat()
p1.pack()

Packer.stat()

print(p1.files)


class Joker():

    def smile(self, smilesize):
        print(" :) " * smilesize)


class SuperPacker(Packer, Joker):
    def __init__(self, method):
        super().__init__(method)


sp = SuperPacker('ZIP')
sp.smile(11)
