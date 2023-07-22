# Создайте функцию генератор чисел Фибоначчи

def fibo(count):
    if count == 0: return
    a, b = 0, 1
    yield a
    for i in range(count-1):
        a, b = b, a + b
        yield a


print(list(fibo(10)))
