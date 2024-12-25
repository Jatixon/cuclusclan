import math


def taylor_sin(x, terms=10):
    """
    Вычисляет синус с помощью разложения в ряд Тейлора.

    x: значение, для которого вычисляется синус (в радианах)
    terms: количество членов ряда Тейлора
    """
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result


def taylor_ln1_minus_x(x, terms=10):
    """
    Вычисляет ln(1-x) с помощью разложения в ряд Тейлора.

    x: значение, для которого вычисляется ln(1-x) (-1 < x <= 1)
    terms: количество членов ряда Тейлора
    """
    if x <= -1 or x > 1:
        raise ValueError("x должен быть в пределах -1 < x <= 1")

    result = 0
    for n in range(1, terms + 1):
        term = (-1) ** (n + 1) * (x ** n) / n
        result += term
    return result


# Пример использования
x_sin = math.radians(30)  # угол в радианах (30 градусов)
approx_sin = taylor_sin(x_sin, terms=10)
actual_sin = math.sin(x_sin)

x_ln = 0.5  # значение для ln(1-x)
approx_ln = taylor_ln1_minus_x(x_ln, terms=10)
actual_ln = math.log(1 - x_ln)

print(f"Приближение с помощью ряда Тейлора для sin(x): {approx_sin}")
print(f"Реальное значение sin(x): {actual_sin}")
print(f"Разница: {abs(approx_sin - actual_sin)}")

print(f"Приближение с помощью ряда Тейлора для ln(1-x): {approx_ln}")
print(f"Реальное значение ln(1-x): {actual_ln}")
print(f"Разница: {abs(approx_ln - actual_ln)}")

