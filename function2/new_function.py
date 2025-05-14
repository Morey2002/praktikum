import time
def task(lym):
    return "first_task " * lym
def sum(a,b):
    return a + b


def mult(a,b):
    return a * b


def div(a,b):
    return a // b


def divide_numbers(x,y):
    if y == 0:
        return "Делить на ноль нельзя"
    else:
        return x / y


def monkey_count(n):
    count_monkey = []
    for i in range(1, n + 1  ):
        count_monkey == count_monkey.append(i)

    return count_monkey


def bouncing_ball(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1

def timer_decorator(func):
    def wrapper (*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнилась за {end_time - start_time:.4f} секунд" )
        return result
    return wrapper

@timer_decorator
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total



def from_string_to_list(string, container):
    numbers = string.split()  # Разбиваем строку по пробелам
    for num in numbers:
        container.append(int(num))

from new_function import *
from higher_func import *
def cakes(recipe, available):
    '''Функция принимает два аргумента рецепт (то что нужно  для приготовления и ингредиенты в наличии)
        На выходе получаем максимальное количество блюд'''

    max_cakes = float('inf')  # Изначально считаем, что можно испечь бесконечно много

    for ingredient, required_amount in recipe.items():  # цикл распаковывающий все значения словаря
        if ingredient not in available:  # проверяем наличие ингридиента в словаре
            return 0  # Если ингредиента нет, сразу возвращаем 0

        available_amount = available[ingredient]  # считаем для каждого элемента сколько тортов можно испечь
        possible_cakes = available_amount // required_amount  # считаем на сколько шт хватит ингредиента

        if possible_cakes < max_cakes:  # проверяем на то что ингредиентов хватает иначе уменьшаем счётчик
            max_cakes = possible_cakes  # присваиваем значение

    return max_cakes  # возвращаем максимальное кол-во


print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
print(cakes({"apples": 3, "flour": 300, "sugar": 100, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
print(task(5))
print(task(4))
print(mult(5, 2))
print(sum(4, 1243))
print(div(5, 2))
print(sum(4,6))

print(calculate_sum(1_000_758))

print("Функции прыжка мяча")
print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))

print("Функции высшего порядка")
print(calculate(summa, 5, 2))
print(calculate(minus, 4, 1243))
print(calculate(divides, 5, 2))
print(calculate(multy, 4, 6))