K, N = map(int, input().split())

def pick(arr):
    if len(arr) == N:
        print(*arr)
    else:
        for i in range(1, K + 1):
            pick(arr + [i])

pick([])