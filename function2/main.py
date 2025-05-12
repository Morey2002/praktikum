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


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))

print("Функции высшего порядка")
print(calculate(summa, 5, 2))
print(calculate(minus, 4, 1243))
print(calculate(divides, 5, 2))
print(calculate(multy, 4, 6))