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

dp = [[False] * (len(s) + 1) for _ in range(len(patterns) + 1)]
dp[0][0] = True

for i in range(len(patterns)):
    for j in range(len(s) + 1):
        if not dp[i][j]:
            continue
        pattern = patterns[i]
        dp[i + 1][j] = True
        if j >= len(s):
            continue
        if len(pattern) == 1:
            if pattern == '.' or pattern == s[j]:
                dp[i + 1][j + 1] = True
        else:
            for k in range(j, len(s)):
                if pattern[0] == '.' or pattern[0] == s[k]:
                    dp[i + 1][k + 1] = True
                else:
                    continue

if dp[-1][-1]:
    print('true')
else:
    print('false')
