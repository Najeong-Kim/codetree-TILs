def is_prime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def is_sum_digits_even(n):
    sum = 0
    while (n):
        sum += n % 10
        n //= 10
    if (sum % 2 == 0):
        return True
    else:
        return False

def func(a, b):
    count = 0
    for i in range(a, b+1):
        if (is_prime(i) and is_sum_digits_even(i)):
            count += 1
    return count

a, b = map(int, input().split())
print(func(a, b))