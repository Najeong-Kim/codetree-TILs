def sum_digit_function(n):
    if n == 0:
        return 0
    return sum_digit_function(n // 10) + n % 10

def multiple_function(a, b, c):
    return sum_digit_function(a * b * c)

a, b, c = map(int, input().split())
print(multiple_function(a, b, c))