s = input()
p = input()

patterns = []
for i in range(len(p)):
    if p[i] == '*':
        continue
    if i < (len(p) - 1) and p[i + 1] == '*':
        patterns.append(p[i:i + 2])
    else:
        patterns.append(p[i])

index = 0
is_same = 'true'

for pattern in patterns:
    if len(pattern) == 1:
        if index >= len(s):
            is_same = 'false'
            break
        if pattern == '.' or pattern == s[index]:
            index += 1
        else:
            is_same = 'false'
            break
    else:
        for i in range(index, len(s)):
            if pattern == '.' or pattern == s[i]:
                index += 1
            else:
                continue

print(is_same)
