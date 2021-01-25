import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CityForm

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    apikey = '*********************'

    

    if request.method == 'POST':
        form = CityForm(request.POST)
        
        
        if form.is_valid():
            city = form.cleaned_data['city_name']
            
            r = requests.get(url.format(city,apikey)).json()
            if r['cod'] != '404':
                city_weather = {
                    'city' : r['name'] ,
                    'temprature' : r['main']['temp'] ,
                    'description' : r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                    'country' : r['sys']['country'],       
                }

                form = CityForm()

                context = {'city_weather' : city_weather , 'form' : form }
            

                return render(request,"weather/weather.html",context)
            else:
                form = CityForm()
                context = {'flag' : 1 , 'form' : form }
                return render(request,"weather/weather.html",context)    
    
    else:

        form = CityForm()

        context = {'form' : form}
    
        return render(request,"weather/weather.html",context)    


        

        

    

