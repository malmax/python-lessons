# -*- coding: utf-8 -*-
"""Малахов Максим."""
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого
# ученика есть два Родителя(мама и папа). Также в школе преподают Учителя,
# один учитель может преподавать в неограниченном кол-ве классов свой
# определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и
# 6Б, но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик
# отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс -->
#  Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    """Абстрактный класс человек."""

    def __init__(self, name):
        """Конструктор."""
        self.name = name

    def __str__(self):
        """Преобразование в строку."""
        return self.name


class Specialization:
    """Специализация преподавателя."""

    def __init__(self, title):
        """Конструктор."""
        self.title = title

    def __str__(self):
        """Приводим к строке."""
        return self.title


class Teacher(Human):
    """Класс Учитель."""

    def __init__(self, name, specialization):
        """Конструктор."""
        Human.__init__(self, name)
        if isinstance(specialization, Specialization):
            self.specialization = specialization
        else:
            raise


class Student(Human):
    """Класс Ученик."""

    def __init__(self, name):
        """Конструктор."""
        Human.__init__(self, name)
        self._parents = []

    def add_parent(self, parent):
        """Добавить родителя."""
        if parent not in self._parents and len(self._parents) < 2:
            if isinstance(parent, Human):
                self._parents.append(parent)

    @property
    def parents(self):
        """Родители."""
        return [str(name) for name in self._parents]


class ClassRoom:
    """Класс школы."""

    def __init__(self, lvl, lvl_chr):
        """Конструктор."""
        self.class_lvl = {"number": int(lvl), "chr": lvl_chr}
        self._students = []
        self._teachers = []

    @property
    def name(self):
        """Название класса."""
        return "{number} {chr}".format(**self.class_lvl)

    def add_student(self, student):
        """Добавить ученика в класс."""
        if student not in self._students:
            if isinstance(student, Student):
                self._students.append(student)

    def lvl_up(self):
        """Переход на следующий год."""
        if self.class_lvl['number'] < 11:
            self.class_lvl['number'] += 1

    def add_teacher(self, teacher):
        """Назначить учителя классу."""
        if isinstance(teacher, Teacher):
            for t in self._teachers:
                if t.specialization == teacher.specialization:
                    return
            self._teachers.append(teacher)

    @property
    def teachers(self):
        """Преподаватели в классе."""
        return [tchr.name for tchr in self._teachers]

    def __str__(self):
        """Преобразование в строку."""
        list1 = []
        list1.append(self.name)
        for std in self._students:
            list1.append(str(std))
        return "\n".join(list1)


class School:
    """Школа."""

    def __init__(self):
        """Конструктор."""
        self._class_roomes = []

    def add_class_room(self, class_room):
        """Добавить класс в школу."""
        if class_room not in self._class_roomes:
            if isinstance(class_room, ClassRoom):
                self._class_roomes.append(class_room)

    @property
    def class_roomes(self):
        """Список классов в школе."""
        return list(clsn.name for clsn in self._class_roomes)

    def get_specializations_for_student(self, std):
        """Получение всех предметов ученика."""
        for clsn in self._class_roomes:
            if std in clsn._students:
                lst = list(str(tchr.specialization) for tchr in clsn._teachers)
                return {"student": str(std), "specializations": lst}

    def __str__(self):
        """Преобразование в строку."""
        list1 = []
        for clsn in self._class_roomes:
            list1.append(str(clsn))
        return "\n".join(list1)


# Студенты
std1 = Student("Иванов Иван Иванович")
std1.add_parent(Human("Иванова Татьяна Леонидовна"))
std1.add_parent(Human("Иванов Иван Семенович"))
std2 = Student("Алексеев Алексей Алексеевич")
std2.add_parent(Human("Алексеева Анастасия Сергеевна"))
std2.add_parent(Human("Алексеев Алексей Семенович"))
std3 = Student("Семенова Мария Сергеевна")
std3.add_parent(Human("Семенова Анастасия Петровна"))
std3.add_parent(Human("Семенов Сергей Иванович"))
std4 = Student("Малахова Вероника Максимовна")
std4.add_parent(Human("Малахова Ирина Николаевна"))
std4.add_parent(Human("Малахов Максим Анатольевич"))
std5 = Student("Сытых Полина Андреевна")
std5.add_parent(Human("Сытых Юлия Николаевна"))
std5.add_parent(Human("Сытых Андрей Данилович"))
# Учителя
tchr1 = Teacher("Родионов Роман Сергеевич", Specialization("Математика"))
tchr2 = Teacher("Владленна Мария Сергеевна", Specialization("География"))
tchr3 = Teacher("Кузьмина Ирина Николаевна", Specialization("Физкультура"))
# Классы
cls1 = ClassRoom(6, "А")
cls1.add_student(std1)
cls1.add_student(std2)
cls1.add_student(std3)
cls1.add_teacher(tchr1)
cls1.add_teacher(tchr3)
cls1.add_teacher(tchr1)
cls2 = ClassRoom(8, "Б")
cls2.add_student(std4)
cls2.add_student(std5)
cls2.add_teacher(tchr2)
cls2.add_teacher(tchr3)
# Школа
school = School()
school.add_class_room(cls1)
school.add_class_room(cls2)


print("Список классов:")
print(school.class_roomes)

print("Список учеников по классам:")
print(school)

print("список всех предметов указанного ученика:")
print(school.get_specializations_for_student(std3))

print("ФИО родителей указанного ученика:")
print(str(std2), std2.parents)

print("Учителей, преподающих в указанном классе:")
print(cls2.name, cls2.teachers)
