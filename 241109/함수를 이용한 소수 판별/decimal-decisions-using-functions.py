def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_sum_prime(a, b):
    result = 0
    for i in range(a, b + 1):
        if is_prime(i):
            result += i
    return result

a, b = map(int, input().split())
print(get_sum_prime(a, b))