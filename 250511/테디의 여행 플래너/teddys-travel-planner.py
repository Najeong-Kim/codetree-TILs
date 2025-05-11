N, Q = map(int, input().split())
cities = list(input().split())

option = []
new_city = [None] * Q

for i in range(Q):
    query = input().split()
    option.append(int(query[0]))
    if option[i] == 4:
        new_city[i] = query[1]

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

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev
    
    u.prev = u.next = None

pin = Node(cities[0])
tail = pin

for i in range(1, N):
    city = Node(cities[i])
    insert_next(tail, city)
    tail = city

tail.next = pin
pin.prev = tail

for i in range(Q):
    if option[i] == 1:
        if pin.next:
            pin = pin.next
    if option[i] == 2:
        if pin.prev:
            pin = pin.prev
    if option[i] == 3:
        if pin.next:
            pop(pin.next)
    if option[i] == 4:
        insert_next(pin, Node(new_city[i]))
    if pin.prev and pin.next:
        if pin.prev.data == pin.next.data:
            print(-1)
        else:
            print(pin.prev.data, pin.next.data)
    else:
        print(-1)