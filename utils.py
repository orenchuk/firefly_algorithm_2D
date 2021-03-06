import math

def distance(firefly, other_firefly):
    return math.sqrt((other_firefly.x - firefly.x) ** 2 + (other_firefly.y - firefly.y) ** 2)

def Ackley_global_minimum(firefly):
    result = firefly.x ** 2 + firefly.y ** 2

    result /= 2
    result = math.sqrt(result)
    result /= -5
    result = -20 * math.exp(result)

    result2 = math.cos(2 * math.pi * firefly.x) + math.cos(2 * math.pi * firefly.y)
    result2 /= 2
    result2 = math.exp(result2) + 20 + math.e

    return result - result2

def Ackley_global_maximum(firefly):
    result = abs(firefly.x) + abs(firefly.y)
    result *= math.exp(-(firefly.x ** 2 + firefly.y ** 2))
    return result

def Michalewicz(firefly):
    return  -(math.sin(firefly.x) * math.sin((firefly.x**2)/math.pi)**20) + -(math.sin(firefly.y) * math.sin((2 * firefly.y**2)/math.pi)**20)

def description(fireflies):
    for i, firefly in enumerate(fireflies):
        print(i, "x:", firefly.x, "y:", firefly.y, "brightness:", firefly.brightness)

def index_of_alpha(fireflies):
    alpha = fireflies[0]
    for firefly in fireflies:
        if firefly.brightness > alpha.brightness:
            alpha = firefly
    return fireflies.index(alpha)