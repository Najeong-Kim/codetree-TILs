def sum_number(n):
    if (n == 1):
        return 1
    return sum_number(n - 1) + n

N = int(input())
print(sum_number(N))