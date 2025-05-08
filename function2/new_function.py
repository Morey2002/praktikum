def task(lym):
    return "first_task " * lym
def sum(a,b):
    return a + b


def min(a,b):
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