N, M = map(int, input().split())
knight = list(map(int, input().split()))
call = [int(input()) for _ in range(M)]

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

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev
    
    u.prev = u.next = None

temp = Node(knight[0])
tail = temp

dict = {}
dict[knight[0]] = temp

for i in range(1, N):
    current_knight = Node(knight[i])
    dict[knight[i]] = current_knight
    insert_next(tail, current_knight)
    tail = current_knight

tail.next = temp
temp.prev = tail

for i in range(M):
    current_knight = dict[call[i]]
    print(current_knight.next.data, current_knight.prev.data)
    pop(current_knight)