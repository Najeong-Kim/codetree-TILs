Q = int(input())

option = []
a = []
b = []

for _ in range(Q):
    query = list(map(int, input().split()))
    option.append(query[0])
    if query[0] == 1 or query[0] == 2:
        a.append(query[1])
        b.append(query[2])
    else:
        a.append(query[1])
        b.append(0)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
def connect(a, b):
    if b is not None:
        b.prev = a
    if a is not None:
        a.next = b

dict = {}
dict[1] = Node(1)
current = 2

for i in range(Q):
    if option[i] == 1:
        head = Node(current)
        tail = head
        dict[current] = head
        current += 1
        for j in range(1, b[i]):
            new_node = Node(current)
            dict[current] = new_node
            tail = new_node
            connect(dict[current - 1], dict[current])
            current += 1
        connect(tail, dict[a[i]].next)
        connect(dict[a[i]], head)

    if option[i] == 2:
        head = Node(current)
        tail = head
        dict[current] = head
        current += 1
        for j in range(1, b[i]):
            new_node = Node(current)
            dict[current] = new_node
            tail = new_node
            connect(dict[current - 1], dict[current])
            current += 1
        connect(dict[a[i]].prev, head)
        connect(tail, dict[a[i]])
    if option[i] == 3:
        student = dict[a[i]]
        if not student.prev or not student.next:
            print(-1)
        else:
            print(student.prev.data, student.next.data)
