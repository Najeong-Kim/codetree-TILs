class User:
    def __init__(self, ID='codetree', Level=10):
        self.ID = ID
        self.Level = Level

(ID, Level) = input().split()

user1 = User()
user2 = User(ID, Level)

def print_user(user):
    print('user ' + user.ID + ' lv ' + str(user.Level))

print_user(user1)
print_user(user2)