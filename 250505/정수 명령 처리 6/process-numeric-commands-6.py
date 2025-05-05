import heapq

N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)

    def pop(self):
        if not self.empty():
            return -heapq.heappop(self.items)
    
    def top(self):
        if not self.empty():
            return -self.items[0]

queue = PriorityQueue()

for command in commands:
    if command[0] == 'push':
        queue.push(command[1])
    if command[0] == 'pop':
        print(queue.pop())
    if command[0] == 'size':
        print(queue.size())
    if command[0] == 'empty':
        print(1 if queue.empty() else 0)
    if command[0] == 'top':
        print(queue.top())
