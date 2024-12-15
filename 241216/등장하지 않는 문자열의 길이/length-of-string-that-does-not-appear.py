N = int(input())
arr = list(input())

result = N

for i in range(1, N + 1):
    dic = []
    is_appeared = False
    for j in range(0, N - i + 1):
        if arr[j:j+i] in dic:
            is_appeared = True
            break
        else:
            dic.append(arr[j:j+i])
    if not is_appeared:
        result = i
        break

print(result)