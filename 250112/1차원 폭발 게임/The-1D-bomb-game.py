n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

while True:
    now = None
    count = 0
    is_deleted = False
    arr = []

    for i in range(len(numbers)):
        if numbers[i] == now:
            count += 1
            if count >= m:
                is_deleted = True
        else:
            if count < m:
                for _ in range(count):
                    arr.append(now)
            now = numbers[i]
            count = 1
    if count >= m:
        is_deleted = True
    else:
        for _ in range(count):
            arr.append(now)
    numbers = arr

    if not is_deleted or not len(numbers):
        break

print(len(numbers))
for number in numbers:
    print(number)