import requests
from datetime import datetime
import locale

FORECAST_LISBON_URL = 'https://api.ipma.pt/public-data/forecast/aggregate/1110600.json'

def get(date = datetime.now().date()):
    forecast_json = http_get(FORECAST_LISBON_URL)

    str_date = date.strftime('%Y-%m-%dT%H:%M:%S')
    day_forecast = [x for x in forecast_json if x['idPeriodo'] == 24 and x['dataPrev'] == str_date]

    tMin = day_forecast[0]['tMin']
    tMax = day_forecast[0]['tMax']
    probabilidadePrecipita = int(float(day_forecast[0]['probabilidadePrecipita']))
    text_date = date.strftime('%d de %B de %Y')
    text_forecast = f"Previsão para dia {text_date}. \
                      Temperatura máxima. {tMax} graus. \
                      Temperatura mínima. {tMin} graus. \
                      Probabilidade de precipitação. {probabilidadePrecipita} por cento."

    return text_forecast

def http_get(url):
    http_response = requests.get(url)

    if http_response.status_code != 200:
        raise Exception("Http error: " + str(http_response.status_code))

    content_type = http_response.headers['content-type']

    if content_type != 'application/json':
        raise Exception("Error: invalid content type " + content_type)

    response = http_response.json()

    return response

locale.setlocale(locale.LC_ALL, 'pt_PT')

# date = datetime.now().date()
# print(get_weather_report(date))
# date = datetime(2023, 10, 26)
# print(get_weather_report(date))
