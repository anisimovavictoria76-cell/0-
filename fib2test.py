import time

def calc_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

print("=== Тестирование граничных значений ===")

test_cases = [
    ("Нижняя граница", 0),
    ("Верхняя граница", 30),
    ("Пример 1", 5),
    ("Пример 2", 10)
]

for name, n in test_cases:
    start = time.time()
    result = calc_fib(n)
    end = time.time()
    print(f"{name}: F({n}) = {result}, время: {end-start:.6f} сек")
