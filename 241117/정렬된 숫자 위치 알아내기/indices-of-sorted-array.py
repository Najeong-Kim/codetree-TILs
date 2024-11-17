n = int(input())
arr = []
input_arr = list(map(int, input().split()))

for i in range(n):
    arr.append((input_arr[i], i + 1))

arr.sort(key=lambda x: x[0])

order = [0] * (n + 1)

for i in range(len(arr)):
    _, index = arr[i]
    order[index] = i + 1

for elem in order[1:]:
    print(elem, end=" ")