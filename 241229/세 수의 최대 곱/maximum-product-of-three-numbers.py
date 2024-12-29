n = int(input())
arr = list(map(int, input().split()))
arr.sort()
plus = list(filter(lambda x: x > 0, arr))
minus = list(filter(lambda x: x < 0, arr))

maximum = arr[0] * arr[1] * arr[2]

if len(plus) >= 3:
    maximum = max(maximum, plus[-1] * plus[-2] * plus[-3])
if len(plus) >= 1 and len(minus) >= 2:
    maximum = max(maximum, plus[-1] * minus[0] * minus[1])
if arr.count(0):
    maximum = max(maximum, 0)
if len(plus) >= 2 and len(minus) >= 1:
    maximum = max(maximum, plus[0] * plus[1] * minus[-1])
if len(minus) >= 3:
    maximum = max(maximum, minus[-1] * minus[-2] * minus[-3])

print(maximum)
