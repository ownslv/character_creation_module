from math import sqrt

message = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа'
)
print(message)


def calculatesquareroot(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Проверяет, что число."""
    if your_number <= 0:
        return
    new_numbers = calculatesquareroot(your_number)
    print(
        f'Мы вычислили квадратный корень из введённого вами числа.'
        f' Это будет: {new_nubmers}'
    )


print(message)
calc(25.5)
