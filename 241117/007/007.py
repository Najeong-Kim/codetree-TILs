class SecretCode:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

a, b, c = map(str, input().split())

secret_code = SecretCode(a, b, c)
print('secret code : ' + secret_code.secret_code)
print('meeting point : ' + secret_code.meeting_point)
print('time : ' + secret_code.time)