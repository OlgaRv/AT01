def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def mulitiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя!')
    return a / b


def check(number):
    return number % 2 == 0


def remainder(a, b):   #  Функция для вычисления остатка от деления a на b.
    if b == 0:
        raise ValueError("Деление на ноль недопустимо.")
    return a % b