from django.shortcuts import render
import requests
# Create your views here.


def index(request):

    city = request.GET.get('city' , 'Delhi')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=964879b2e4be94497f61156da3b284d5'
    data = requests.get(url).json()

    payload = {
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelvin_temprature' : data['main']['temp'],
        'celcius_temprature': int(data['main']['temp']) - 273,
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
      }

    context = {'data' : payload}
    print(context)

    return render(request, 'index.html', context)