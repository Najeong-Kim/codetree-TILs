parenthesis = input()

count = 0

for i in range(len(parenthesis) - 1):
    for j in range(i + 2, len(parenthesis) - 1):
        if parenthesis[i] == '(' and parenthesis[i + 1] == '(' and parenthesis[j] == ')' and parenthesis[j + 1] == ')':
            count += 1

print(count)