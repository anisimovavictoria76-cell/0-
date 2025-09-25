import time

def fib_last_digit(n):
    if n == 0 or n == 1:
        return n
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr

tests = [0, 331, 327305, 10000000]

for n in tests:
    start = time.time()
    result = fib_last_digit(n)
    end = time.time()
    print(f"n={n}: цифра={result}, время={end-start:.4f}сек")
