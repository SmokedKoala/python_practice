"""
Некто попытался реализовать "наивную" функцию умножения с помощью сложения.
К сожалению, в коде много ошибок. Сможете ли вы их исправить?
Добавьте к naive_mul автоматическое тестирование для проверки обоих
аргументов в диапазоне от 0 до 100. Сравнивайте с встроенным умножением,
используя конструкцию assert.
"""

def naive_mul(x, y, res=0):
    for _ in range(y):
        res += x
    return res

def test_naive_mul():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("native_mul succeed")

test_naive_mul()


"""
Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного умножения в
столбик. Добавьте автоматическое тестирование, как в случае с naive_mul.
"""

def fast_mul(x, y, res=0):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return res + y
    if x % 2 != 0:
        res += y
    return fast_mul(x // 2, y * 2, res)

def test_fast_mul():
    for x in range(101):
        for y in range(101):
            assert fast_mul(x, y) == x * y
    print("fast_mul succeed")

test_fast_mul()


"""
Реализуйте аналогичную функцию fast_pow для возведения в степень (её легко
получить из предыдущего решения).
"""

def fast_pow(x, y, res=1):
    while y > 0:
        if y == 1:
            return res * x
        if y % 2 != 0:
            res *= x
        x *= x
        y //= 2
    return res

def test_fast_pow():
    for x in range(101):
        for y in range(101):
            assert fast_pow(x, y) == x ** y
    print("fast_pow succeed")


test_fast_pow()