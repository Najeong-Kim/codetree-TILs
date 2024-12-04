import sys

N = int(input())

checkpoints = [list(map(int, input().split())) for _ in range(N)]

min_distance = sys.maxsize

for i in range(1, N - 1):
    skipped = checkpoints[:i] + checkpoints[i + 1:]
    distance = 0

    for j in range(len(skipped) - 1):
        distance += abs(skipped[j][0] - skipped[j + 1][0]) + abs(skipped[j][1] - skipped[j + 1][1])
    min_distance = min(distance, min_distance)

print(min_distance)