arr = list(map(int, input().split()))
arr.sort()

def get_list(A, B, C, D):
    return [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            for l in range(k + 1, len(arr)):
                cur = get_list(arr[i], arr[j], arr[k], arr[l])
                cur.sort()
                if arr == cur:
                    print(arr[i], arr[j], arr[k], arr[l])
                    exit(0)
