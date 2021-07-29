import requests

print('Выберите город, по которому хотите узнать погоду:\n1 - Санкт-Петербург\n2 - Москва\n3 - Сочи')

user_choice = input()

if user_choice == '1':
    response = requests.get(f'https://api.weatherbit.io/v2.0/current?city=Petersburg&country=RU&lang=ru&key=e5161f9689044a429c2d811245b6cb6f')
    response_js = response.json()
    print('В Питере '+ str(response_js['data'][0]['temp']) + ' градусов по цельсию')
elif user_choice == '2':
    response = requests.get(f'https://api.weatherbit.io/v2.0/current?city=Moscow&country=RU&lang=ru&key=e5161f9689044a429c2d811245b6cb6f')
    response_js = response.json()
    print('В Москве '+ str(response_js['data'][0]['temp']) + ' градусов по цельсию')
else:
    response = requests.get(
        f'https://api.weatherbit.io/v2.0/current?city=Sochi&country=RU&lang=ru&key=e5161f9689044a429c2d811245b6cb6f')
    response_js = response.json()
    print('В Сочи '+ str(response_js['data'][0]['temp']) + ' градусов по цельсию')