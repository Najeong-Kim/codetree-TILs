S_init = input()
N = int(input())

command = []
S_value = []

for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)
    if cmd == 1 or cmd == 2:
        S_value.append(line[1])
    else:
        S_value.append("")

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
def insert_next(u, singleton):
    singleton.prev = u
    singleton.next= u.next

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton
    
def insert_prev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev
    
    u.prev = u.next = None

node = Node(S_init)
for i in range(N):
    new_node = Node(S_value[i])
    if command[i] == 1:
        insert_prev(node, new_node)
    if command[i] == 2:
        insert_next(node, new_node)
    if command[i] == 3:
        if node.prev:
            node = node.prev
    if command[i] == 4:
        if node.next:
            node = node.next
    if node.prev:
        print(node.prev.data, end=' ')
    else:
        print('(Null)', end=' ')
    print(node.data, end=' ')
    if node.next:
        print(node.next.data)
    else:
        print('(Null)')
