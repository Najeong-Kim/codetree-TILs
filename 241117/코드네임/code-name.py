class Codename:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

codenames = []

for _ in range(5):
    codename, score = input().split()
    codenames.append(Codename(codename, score))

def get_lowest():
    result = codenames[0]
    for i in range(len(codenames)):
        if int(result.score) > int(codenames[i].score):
            result = codenames[i]
    return result

lowest = get_lowest()

print(f"{lowest.codename} {lowest.score}")