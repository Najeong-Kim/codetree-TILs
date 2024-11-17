class BombDefusal:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = input().split()

bomb_defusal = BombDefusal(code, color, second)
print('code : ' + bomb_defusal.code)
print('color : ' + bomb_defusal.color)
print('second : ' + bomb_defusal.second)