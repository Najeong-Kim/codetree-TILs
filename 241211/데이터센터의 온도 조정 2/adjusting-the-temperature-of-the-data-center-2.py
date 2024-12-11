N, C, G, H = map(int, input().split())
temperatures = [list(map(int, input().split())) for _ in range(N)]

def select_workload(temperature, a, b):
    if temperature < a:
        return C
    elif a <= temperature <= b:
        return G
    else:
        return H

count = 0

for i in range(1001):
    current = 0
    for temperature in temperatures:
        current += select_workload(i, temperature[0], temperature[1])
    count = max(count, current)

print(count)