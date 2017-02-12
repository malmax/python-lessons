# -*- coding: utf-8 -*-
"""Малахов Максим."""
import urllib
import gzip
import json
import sys
from grab import Grab


""" OpenWeatherMap
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API для
доступа к данным о текущей погоде, прогнозам, для web-сервисов и мобильных
приложений. Архивные данные доступны только на коммерческой основе. В
качестве источника данных используются официальные метеорологические
службы, данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, используя дополнительную
    библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ вытащить со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"
"""
req = sys.argv


class WeatherConnect:
    """Соединение с сервером погоды."""

    def __init__(self, email, password):
        """Конструктор."""
        self.g = Grab()
        self.g.setup(connect_timeout=20, timeout=20)
        self.__email = email
        self.__password = password
        self.__isLogin = False
        self.auth()

    def auth(self):
        """Аутентификация на сервере."""
        print("auth")
        self.g.go('https://home.openweathermap.org/users/sign_in')
        self.g.doc.set_input_by_id('user_email', self.__email)
        self.g.doc.set_input_by_id('user_password', self.__password)
        self.g.doc.submit()
        if self.g.doc.code == 200:
            self.__isLogin = True

    def get_keys(self, arg=None):
        """Получение ключей и запись в файл."""
        if self.__isLogin:
            print("take api keys")
            self.g.go('https://home.openweathermap.org/api_keys')
            api_keys = [x.text for x in self.g.css_list('.api-keys td pre')]
            with(open('app.id', 'w', encoding='utf-8')) as f:
                f.write('\n'.join(api_keys))

    def download_cities(self, arg=None):
        """Загружаем архив с городами и распаковываем его."""
        print("get cities")
        url = "http://bulk.openweathermap.org/sample/city.list.json.gz"

        with(urllib.request.urlopen(url)) as u:
            gz = u.read()
        # записываем архив
        with(open("city.list.json.gz", "wb")) as f:
            f.write(gz)
        # распаковываем
        with(gzip.open("city.list.json.gz", "rb")) as f_in:
            data_content = f_in.read()

        with(open("city.list.json", "w", encoding='UTF-8')) as f_out:
            f_out.write(data_content)

    def get_all_cities(self):
        """Получение всех городов."""
        with(open("city.list.json", "r", encoding='UTF-8')) as f:
            read = f.read()
        return json.load(read)

    def get_cities_by_country(self, country='RU'):
        """Загрузка всех городов по стране."""
        print(list(filter(lambda x: x.country == country, self.get_all_cities())))


weather = WeatherConnect('malmax.spb@gmail.com', 'malmaster')

do = {
    'getkeys': weather.get_keys,
    'getcities': weather.download_cities,
    'getcitiesbycountry': weather.get_cities_by_country}

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    second_arg = sys.argv[2]
except IndexError:
    second_arg = None


if do.get(key):
    do[key](second_arg)
else:
    print("Задан неверный ключ")
    for key, value in do.items():
        print(key, ' - ', value)


"""
== Получение списка городов ==
    Список городов может быть получен по ссылке:
     http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
        (воспользоваться модулем gzip или вызвать распаковку через создание
        процесса архиватора через модуль subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
    {"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
    {"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут
     как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},"weather":[{"id":803,"main":"Clouds",
    "description":"broken clouds","icon":"04n"}],"base":"cmc stations",
    "main":{"temp":280.03,"pressure":1006,"humidity":83,"temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},"rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,"sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,"sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite с следующей структурой данных (если файла
   базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик имеет смысл запрашивать
 у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами
- используется созданная база данных, новые данные добавляются и обновляются



При работе с XML-файлами:

Доступ к данным в XML файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
