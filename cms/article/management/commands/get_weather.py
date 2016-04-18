from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    """Show current weather in console

    Get weather data from openweathermap
    And print current temperature, humidity and commot weather data in console
    """
    help = "Get weather by city name"
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('city')

    def handle(self, *args, **options):
        from django.conf import settings
        city = options['city']

        open_weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'

        res = requests.get(open_weather_url.format(
            city=city,
            appid=settings.OPEN_WEATHER_API_KEY)
        )
        weather = res.json()

        print """
        City - {name}
        {description}
        Temperature - {temp} C
        Humidity - {humidity} %
        """.format(
            name=weather['name'],
            description=weather['weather'][0]['description'].title(),
            humidity=weather['main']['humidity'],
            temp=weather['main']['temp'] - 273.15
        )
