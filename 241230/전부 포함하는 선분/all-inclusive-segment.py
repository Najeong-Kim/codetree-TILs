n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(lambda x: x[0])
start = arr[1][0]
end = max(list(map(lambda x: x[1], arr[1:])))

arr.sort(lambda x: x[1])
start2 = min(list(map(lambda x: x[0], arr[:-1])))
end2 = arr[-2][1]

print(min(end - start, end2 - start2))