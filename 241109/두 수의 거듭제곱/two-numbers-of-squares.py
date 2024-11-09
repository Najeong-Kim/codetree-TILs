def power(a, b):
    result = 1
    for i in range(0, b):
        result *= a
    return result

a, b = map(int, input().split())
print(power(a, b))