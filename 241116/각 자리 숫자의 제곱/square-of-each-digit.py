def sum_digit(n):
    if n <= 9:
        return n ** 2
    return sum_digit(n // 10) + (n % 10) ** 2

N = int(input())
print(sum_digit(N))