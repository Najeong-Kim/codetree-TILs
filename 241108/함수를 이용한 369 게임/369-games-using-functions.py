def is_correct_condition(n):
    return (n % 10) % 3 == 0 or (n // 10) % 3 == 0 or n % 3 == 0

def count_369(a, b):
    count = 0
    for i in range(a, b + 1):
        if is_correct_condition(i):
            count += 1
    return count

a, b = map(int, input().split())
result = count_369(a, b)
print(result)