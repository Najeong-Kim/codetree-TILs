class Weather:
    def __init__(self, year, month, date, day, weather):
        self.year = year
        self.month = month
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
weather_list = []

for i in range(n):
    full_date, day, weather = input().split()
    year, month, date = full_date.split('-')
    weather_list.append(Weather(year, month, date, day, weather))

weather_list.sort(key=lambda x: (x.year, x.month, x.date))

for weather in weather_list:
    if weather.weather == 'Rain':
        print(f"{weather.year}-{weather.month}-{weather.date} {weather.day} {weather.weather}")
        break
