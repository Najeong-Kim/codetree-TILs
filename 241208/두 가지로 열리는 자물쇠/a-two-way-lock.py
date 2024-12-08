N = int(input())
a, b, c = list(map(int, input().split()))
a2, b2, c2 = list(map(int, input().split()))

total = 0

def is_satisfied(lock, key):
    if key in get_list(lock):
        return True
    return False

def get_list(a):
    arr = []
    arr.append(a - 1 + N if a - 1 < 1 else a - 1)
    arr.append(a - 2 + N if a - 2 < 1 else a - 2)
    arr.append(a)
    arr.append(a + 1 - N if a + 1 > N else a + 1)
    arr.append(a + 2 - N if a + 2 > N else a + 2)
    return arr


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if is_satisfied(a, i) and is_satisfied(b, j) and is_satisfied(c, k):
                total += 1
                continue
            if is_satisfied(a2, i) and is_satisfied(b2, j) and is_satisfied(c2, k):
                total += 1

print(total)