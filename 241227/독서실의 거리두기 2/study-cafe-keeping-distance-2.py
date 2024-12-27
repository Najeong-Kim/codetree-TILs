import math

N = int(input())
seats = list(input())
start, end = 0, 0

for i in range(len(seats)):
    if seats[i] == '1':
        start = i
        break

for i in reversed(range(len(seats))):
    if seats[i] == '1':
        end = i
        break

def get_distance(seats, isMax = True):
    now = 0
    distance = 0 if isMax else 1000
    for i in range(1, len(seats)):
        now += 1
        if seats[i] == '1':
            distance = max(now, distance) if isMax else min(now, distance)
            now = 0
    return distance

start_distance = start
end_distance = len(seats) - 1 - end
between_distance = math.floor(get_distance(seats) / 2)
default_distance = get_distance(seats, False)

if start_distance >= between_distance or end_distance >= between_distance:
    print(max(min(start_distance, default_distance), min(end_distance, default_distance)))
else:
    print(min(between_distance, default_distance))