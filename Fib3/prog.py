def calc_fib_last_digit(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10  
    return b

with open('input.txt', 'r') as input_file:
    n = int(input_file.read().strip())

result = calc_fib_last_digit(n)

with open('output.txt', 'w') as output_file:
    output_file.write(str(result))