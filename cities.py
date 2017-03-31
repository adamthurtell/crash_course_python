cities = {
    'kathmandu': {
        'country': 'nepal',
        'population': 1081845,
        'fact': 'people poop in each other\'s mouths',
    },
    'detroit': {
        'country': 'united state',
        'population': 'popdetroit',
        'fact': 'factdetroit',
    },
    'london': {
        'country': 'england',
        'population': 'poplondon',
        'fact': 'factlondon',
    },
}

for city_name, city_info in cities.items():
    print("\nHere is some information about " + city_name.title() + ":")
    country_name = city_info['country']
    city_pop = city_info['population']
    fun_fact = city_info['fact']
    print(city_name.title() + " is in " + country_name.title() +
          " and has a population of " + str(city_pop) + ". A fun fact about " +
          city_name.title() + ": " + fun_fact + ".")