N = int(input())
Q = int(input())

type_arr = []
i_arr = []
j_arr = []

for _ in range(Q):
    query = list(map(int, input().split()))
    type_arr.append(query[0])
    i_arr.append(query[1])
    if query[0] in [2, 3]:
        j_arr.append(query[2])
    else:
        j_arr.append(0)

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

dict = {}

for i in range(1, N + 1):
    dict[i] = Node(i)

for i in range(Q):
    if type_arr[i] == 1:
        pop(dict[i_arr[i]])
    if type_arr[i] == 2:
        insert_prev(dict[i_arr[i]], dict[j_arr[i]])
    if type_arr[i] == 3:
        insert_next(dict[i_arr[i]], dict[j_arr[i]])
    if type_arr[i] == 4:
        if dict[i_arr[i]].prev:
            print(dict[i_arr[i]].prev.data, end=' ')
        else:
            print(0, end=' ')
        if dict[i_arr[i]].next:
            print(dict[i_arr[i]].next.data)
        else:
            print(0)

for i in range(1, N + 1):
    if dict[i].next:
        print(dict[i].next.data, end=' ')
    else:
        print(0, end=' ')
