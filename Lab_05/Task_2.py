import json
import requests
from urllib.request import urlopen

url = 'https://date.nager.at/api/v3/PublicHolidays/2023/AT'
available_countries = 'https://date.nager.at/api/v3/AvailableCountries'
# av_countries_response = urlopen(available_countries)
with urlopen(available_countries) as avc:
    countries_dict = json.load(avc)
    print(countries_dict)
    print(type(countries_dict))
# print(type(av_countries_response))
# countries_json = json.loads(av_countries_response)
# print(type(countries_json))
# select_country = input ("Enter the country: ")


def get_country_code_from_country_name(country):
    for key, value in countries_json.items():
        if country == value:
            return key
    return "This country is not available."
    
# print(get_country_code_from_country_name(select_country))

# type_year = input('Type the year to see public holidays: ')
# type_country_code = 
# request_date = requests.get(available_countries, params={})
# print(request_date.json())