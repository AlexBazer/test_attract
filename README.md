### Set up and start project

## Install requirements
```
    pip install -r requirements.txt
```
## Run project migrations
```
    ./cms/manage.py migrate
```
## Load fixtures
```
    ./cms/manage.py loaddata ./cms/article/fixtures/all.json
```

## Run project locally on port 8000
```
    ./cms/manage.py runserver
```

### Project commands
## Get weather command
Weather from openweathermap used. Service have restrictions http://openweathermap.org/appid
```
    ./cms/manage.py get_weather <city_name>
```
