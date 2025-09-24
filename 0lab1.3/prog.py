with open('input.txt', 'r') as f_input:
    line = f_input.readline()
    numbers = line.split()
    a = int(numbers[0])
    b = int(numbers[1])

result = a + b

with open('output.txt', 'w') as f_output:
    f_output.write(str(result))