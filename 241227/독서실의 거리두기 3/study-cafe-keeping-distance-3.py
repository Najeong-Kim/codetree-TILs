import math

N = int(input())
seats = list(input())

def get_distance(seats, isMax = True):
    now = 0
    distance = 0 if isMax else 1000
    for i in range(1, len(seats)):
        now += 1
        if seats[i] == '1':
            distance = max(now, distance) if isMax else min(now, distance)
            now = 0
    return distance

print(min(math.ceil(get_distance(seats) / 2), get_distance(seats, False)))
