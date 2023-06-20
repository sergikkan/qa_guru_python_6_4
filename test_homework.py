import random
from math import pi


def test_greeting():
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = "Привет, "+name+"! Тебе "+age+" лет"
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20

    perimeter = (a + b) * 2
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    # TODO сосчитайте площадь
    area = pi * (r ** 2)
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * pi * r
    assert length == 144.51326206513048


def test_random_list():
    # TODO создайте список
    l1 = random.sample(range(1, 100), 10)
    l1.sort()
    assert len(l1) == 10
    assert l1[0] < l1[-1]


def test_unique_elements():
    l1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l1 = set(l1)
    l1 = list(l1)
    assert isinstance(l1, list)
    assert len(l1) == 10
    assert l1 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    assert isinstance(d, dict)
    assert len(d) == 5
