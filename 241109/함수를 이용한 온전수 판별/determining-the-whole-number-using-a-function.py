def is_whole_number(n):
    if (n % 2 == 0):
        return False
    if (n % 10 == 5):
        return False
    if (n % 3 == 0 and n % 9 != 0):
        return False
    return True

def func(a, b):
    count = 0
    for i in range(a, b+1):
        if (is_whole_number(i)):
            count += 1
    return count

a, b = map(int, input().split())
print(func(a, b))