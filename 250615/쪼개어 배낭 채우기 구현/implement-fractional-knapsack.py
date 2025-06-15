N, M = map(int, input().split())
arr = []
for i in range(N):
    w, v = map(int, input().split())
    arr.append([v / w, w, v])

arr.sort(lambda x: -x[0])

result = 0
index = 0
bag = M
while bag > 0:
    p, w, v = arr[index]
    if bag >= w:
        result += v
        index += 1
        bag -= w
    else:
        result += p * bag
        break

print(f"{result:.3f}")