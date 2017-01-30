# -*- coding: utf-8 -*-
"""ДЗ Normal Студента: Малахов Максим."""
import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    """Возвращает последовательность Фибоначи."""
    fibonacci = [1, 1]
    if(n > m):
        return

    def nextNum(n1=1, n2=1):
        """Следующее число Фибоначи."""
        return n1 + n2

    for i in range(len(fibonacci), m):
        n1 = fibonacci[i-2] or 1
        n2 = fibonacci[i-1] or 1
        fibonacci.append(nextNum(n1, n2))

    return fibonacci[n-1:]


print(fibonacci(1, 5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод
# sort()


def sort_to_max(origin_list):
    """Сортировка списка по возрастанию."""
    for i in range(len(origin_list)):
        # Если предыдущий элемент меньше текущего - меняем местами
        for j in reversed(range(i + 1)):
            if(j > 0 and origin_list[j-1] > origin_list[j]):
                temp = origin_list[j-1]
                origin_list[j-1] = origin_list[j]
                origin_list[j] = temp

    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def customFilter(callback, list):
    """Собственный вариант Filter."""
    newList = []
    for i in list:
        if callback(i):
            newList.append(i)
    return newList


print(customFilter(lambda x: x > 1, [1, 2, 3]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def isParallelogram(points):
    """Определение параллелограмма."""
    a = points[0]
    b = points[1]
    c = points[2]
    d = points[3]

    ab = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    cd = math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)
    bc = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
    da = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)

    return(ab == cd and bc == da)


print(isParallelogram([(0, 0), (0, 2), (2, 2), (2, 0)]))
