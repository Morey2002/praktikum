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

