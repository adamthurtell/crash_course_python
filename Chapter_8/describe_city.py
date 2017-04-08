def describe_city(city_name, city_country='Canada'):
    """Desribe a city in a country, with the default country of Canada"""
    print("\n" + city_name.title() + " is in " + city_country.title() + ".")

describe_city('Toronto')