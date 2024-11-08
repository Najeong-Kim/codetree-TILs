def is_correct_condition(n):
    result = False
    for i in range(len(str(n))):
        if int(str(n)[i]) in [3, 6, 9]:
            result = True
    if (n % 3 == 0):
        result = True
    return result

def count_369(a, b):
    count = 0
    for i in range(a, b + 1):
        if is_correct_condition(i):
            count += 1
    return count

a, b = map(int, input().split())
result = count_369(a, b)
print(result)