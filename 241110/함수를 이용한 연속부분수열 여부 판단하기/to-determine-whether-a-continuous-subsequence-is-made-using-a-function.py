def is_subsequence(a, b):
    for i in range(0, len(a) - len(b) + 1):
        result = True
        for j in range(0, len(b)):
            if a[i+j] != b[j]:
                result = False
                break
        if result == True:
            return 'Yes'
    return 'No'

n_a, n_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(is_subsequence(a, b))