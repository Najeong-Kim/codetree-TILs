K, N = map(int, input().split())
arr = []

def pick():
    global arr
    if len(arr) == N:
        print(*arr)
    else:
        for i in range(1, K + 1):
            if len(arr) <= 1 or not (arr[-2] == i and arr[-1] == i):
                arr.append(i)
                pick()
                arr.pop()

pick()
