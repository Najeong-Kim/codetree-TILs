class Individual:
    def __init__(self, name, number, region):
        self.name = name
        self.number = number
        self.region = region

n = int(input())
individual_list = []

for i in range(n):
    name, number, region = input().split()
    individual_list.append(Individual(name, number, region))

individual_list.sort(key=lambda x : x.name)

last = individual_list[-1]
print(f"name {last.name}")
print(f"addr {last.number}")
print(f"city {last.region}")