from collections import deque
N, G = map(int, input().split())

group = []
finished = [False] * G
group_size = []
attend = [[] for _ in range(N + 1)]
attended = [False] * (N + 1)

for j in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(set(nums[1:]))
    for i in range(1, len(nums)):
        attend[nums[i]].append(j + 1)

received = set([1])
queue = deque([1])
attended[1] = True
while len(queue):
    person = queue.popleft()
    now_attend = attend[person]
    
    for now_group in now_attend:
        if finished[now_group - 1]:
            continue
        diff = list(group[now_group - 1].difference(received))
        if len(diff) == 1:
            received.add(diff[0])
            finished[now_group - 1] = True
            if not attended[diff[0]]:
                queue.append(diff[0])
                attended[diff[0]] = True

print(len(received))
