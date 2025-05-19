from collections import deque
N, G = map(int, input().split())

group = []
finished = [False] * G
group_size = []
attend = [[] for _ in range(N + 1)]

for j in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(set(nums[1:]))
    for i in range(1, len(nums)):
        attend[nums[i]].append(j + 1)

received = set([1])
queue = deque([1])
while len(queue):
    person = queue.popleft()
    now_attend = attend[person]
    
    for now_group in now_attend:
        count = 0
        result = 0
        if finished[now_group - 1]:
            continue
        for i in group[now_group - 1]:
            if i not in received:
                count += 1
                result = i
        if count == 1:
            received.add(result)
            finished[now_group - 1] = True
            queue.append(result)

print(len(received))
