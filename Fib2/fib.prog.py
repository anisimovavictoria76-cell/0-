def calc_fib(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

with open('fib.input.txt', 'r') as input_file:
    n = int(input_file.read().strip())

result = calc_fib(n)

with open('fib.output.txt', 'w') as output_file:
    output_file.write(str(result))