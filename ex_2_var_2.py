"""
Задание 1. Вариант 2
Разработать программу для вычисления выражения и вывода полученного результата.
Соответствующие исходные данные ввести с клавиатуры.
"""


import math


def main():
    x, y = get_nums()
    h = calc_h(x, y)
    print("результат:", h)


def get_nums() -> tuple[float, float]:
    while True:
        try:
            x = float(input("Введите x: "))
            y = float(input("Введите y: "))
            return x, y
        except ValueError:
            print("Некорректный ввод. Введите число")


def calc_h(x: float, y: float) -> float:
    if x < y:
        h = math.atan(x + abs(y))
    elif x > y:
        h = math.atan(abs(x)) + y
    else:
        h = pow((x + y), 2)
    return h


if __name__ == "__main__":
    main()
