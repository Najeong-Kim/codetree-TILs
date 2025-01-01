n = int(input())
arr = list(map(int, input().split()))

k = len(str(max(arr)))

for i in range(k):
    new_arr = [[] for _ in range(10)]
    for j in range(len(arr)):
        if arr[j] >= 10 ** i:
            new_arr[int(str(arr[j])[i])].append(arr[j])
        else:
            new_arr[0].append(arr[j])
    temp = []
    for elem in new_arr:
        for elem2 in elem:
            temp.append(elem2)
    arr = temp

for elem in arr:
    print(elem, end=' ')