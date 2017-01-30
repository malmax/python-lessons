# -*- coding: utf-8 -*-
"""ДЗ Easy Студента: Малахов Максим."""

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам
# (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):
    """Округление числа."""
    number = number * 10 ** ndigits
    floatPart = number % 1

    if(floatPart >= 0.5):
        return (number + 1 - floatPart) / 10 ** ndigits
    else:
        return (number - floatPart) / 10 ** ndigits


print(my_round(2.1234567, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    """Счастливый билет."""
    t1 = int(ticket_number / 1000)
    t2 = int(ticket_number % 1000)

    def sum(num):
        """Суммирует числа."""
        if(num > 10):
            return num % 10 + sum((num - num % 10) / 10)
        else:
            return num

    return sum(t2) == sum(t1)


print(lucky_ticket(345903))
