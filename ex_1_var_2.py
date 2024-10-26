"""
Задание 1. Вариант 2
Предусмотрите проверку деления на ноль.
Все необходимые переменные пользователь вводит через консоль.
Запись |пример| означает «взять по модулю», т.е. если значение получится отрицательным,
необходимо сменить знак с минуса на плюс.
"""


import math


def main():
    # Получение значений переменных
    x, y = get_nums()
    # Расчет значения по примеру
    d = calc_expression(x, y)
    print(d)


def get_nums() -> tuple[float, float]:
    while True:
        try:
            x = float(input("Введите x: "))
            y = float(input("Введите y: "))
            return x, y
        except ValueError:
            print("Некорректный ввод. Введите число")


def calc_expression(x: float, y: float) -> float:
    try:
        d = (2 * math.cos(x - math.pi / 6)) / (0.5 + math.pow(math.sin(y), 2)) + abs(y - x)
        return d
    except ZeroDivisionError:
        print("Деление на ноль невозможно. Задача не может быть решена с данными значениями переменныых")


if __name__ == "__main__":
    main()
