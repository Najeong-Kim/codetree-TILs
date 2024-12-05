N = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i, N):
        new_arr = []
        for k in range(i, j + 1):
            new_arr.append(arr[k])
        average = sum(new_arr) / len(new_arr)
        if average in new_arr:
            count += 1

print(count)
