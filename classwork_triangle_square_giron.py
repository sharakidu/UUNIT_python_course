"""
добавил: функцию main, возможность задать количество треугольников,
их валидацию, проверку на равнобедренность и выыод площадей всех введенных треугольников
"""


def main():
    triangle_squares = []
    num_triangles = int(input("Введите количество треугольников: "))
    for n in range(num_triangles):
        print("Введите стороны треугольника", n + 1)
        a, b, c = input_data_for_calculate_giron()
        print(check_triangle_type(a, b, c))
        triangle_squares.append(calc_square_giron(a, b, c))
    print("Площади введенных треугольников:")
    for i in range(len(triangle_squares)):
        print(f"Площадь треугольника {i + 1} равна {triangle_squares[i]:.2f}")


def calc_square_giron(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    triangle_square = (p * (p - a)*(p - b) * (p - c)) ** 0.5
    print(f"Площадь нового треугоьника по ф-ле Гирона: {triangle_square:.2f}")
    return triangle_square


def input_data_for_calculate_giron():
    flag = True
    while flag:
        print()
        a = float(input("Введите сторону треугольника: "))
        b = float(input("Введите сторону треугольника: "))
        c = float(input("Введите сторону треугольника: "))
        if validate_triangle(a, b, c):
            return a, b, c
        else:
            print("треугольника с такими сторонами не существует")


def validate_triangle(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b < c or a + c < b or b + c < a:
        return False
    else:
        return True


def check_triangle_type(a, b, c) -> str:
    if a == b == c:
        return "треугольник равносторонний"
    elif a == b and a == c or b == c and a == b or a == c and b == c:
        return "треугольник равнобедренный"
    else:
        return "треугольник не равнобедренный"


if __name__ == "__main__":
    main()
