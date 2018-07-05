from django.shortcuts import render
from weather import Weather

# Create your views here.
def index(request):
    "View for home page without any data."
    return render(request,'HomePage.html')

def info(request):
    "View for page with the forecast."
    weather=Weather()
    city=request.POST["City_Name"]
    location = weather.lookup_by_location(city)
    forecasts = location.forecast
    return render(request,'ResultsPage.html',{"forecasts":forecasts,'City':city})
