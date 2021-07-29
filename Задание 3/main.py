import requests

print('Выберите город, по которому хотите узнать погоду:\n1 - Санкт-Петербург\n2 - Москва\n3 - Сочи')

user_choice = input()

def request(city):
    response = requests.get(f'https://api.weatherbit.io/v2.0/current?city={city}&country=RU&lang=ru&key=e5161f9689044a429c2d811245b6cb6f')
    response_js = response.json()
    print(f'В {city} ' + str(response_js['data'][0]['temp']) + ' градусов по цельсию')


if user_choice == '1':
    request('Petersburg')
elif user_choice == '2':
    request('Moscow')
else:
    request('Sochi')
