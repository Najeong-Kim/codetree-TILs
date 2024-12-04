n = int(input())
arr = [input() for _ in range(n)]

result = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a, b, c = arr[i], arr[j], arr[k]
            max_len = max(len(a), len(b), len(c))
            a = '0' * (max_len - len(a)) + a
            b = '0' * (max_len - len(b)) + b
            c = '0' * (max_len - len(c)) + c
            has_carry = False
            for l in range(max_len):
                if int(a[l]) + int(b[l]) + int(c[l]) >= 10:
                    has_carry = True
                    break
            if not has_carry:
                result = max(result, int(a) + int(b) + int(c))

print(result)