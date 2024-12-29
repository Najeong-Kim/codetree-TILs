N = int(input())
arr = [int(input()) for _ in range(N)]
distance = max(arr) - min(arr)

def check_distance(position):
    count = 0
    for elem in arr:
        count += abs(elem - position)
    return count

if distance % 2 == 0:
    print(check_distance(distance / 2) // 2)
else:
    print(min(check_distance(distance // 2), check_distance((distance // 2) + 1)) // 2)