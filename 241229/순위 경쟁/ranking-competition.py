n = int(input())

score = {
    'A': 0,
    'B': 0,
    'C': 0
}
rank = ['A', 'B', 'C']
count = 0

def check_rank(score):
    if score['A'] == score['B'] == score['C']:
        return ['A', 'B', 'C']
    elif score['A'] == score['B'] and score['A'] > score['C']:
        return ['A', 'B']
    elif score['A'] == score['C'] and score['A'] > score['B']:
        return ['A', 'C']
    elif score['B'] == score['C'] and score['B'] > score['A']:
        return ['B', 'C']
    elif score['A'] > score['B'] and score['A'] > score['C']:
        return ['A']
    elif score['B'] > score['A'] and score['B'] > score['C']:
        return ['B']
    elif score['C'] > score['A'] and score['C'] > score['B']:
        return ['C']

for i in range(n):
    c, s = input().split()
    score[c] += int(s)
    now = check_rank(score)
    if rank != now:
        count += 1
        rank = now

print(count)
