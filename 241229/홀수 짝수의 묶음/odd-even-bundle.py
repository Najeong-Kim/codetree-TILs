N = int(input())
arr = list(map(int, input().split()))
odd = 0
even = 0
isEvenOrder = True
count = 0

# 짝 == 홀
# 짝 == 홀 + 1

for elem in arr:
    if elem % 2 == 0:
        even += 1
    else:
        odd += 1

while True:
    if odd == even:
        print(odd + even)
        break
    elif odd < even:
        print(odd * 2 + 1)
        break
    else:
        odd -= 2
        even += 1
