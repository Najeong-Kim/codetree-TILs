parenthesis = input()

count = 0

for i in range(len(parenthesis)):
    for j in range(i + 1, len(parenthesis)):
        if parenthesis[i] == '(' and parenthesis[j] == ')':
            count += 1

print(count)
