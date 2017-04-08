def city_country(city_name, country_name):
    """Returns a formatted city and country"""
    city_and_country = city_name + ", " + country_name
    return city_and_country.title()

while True:
    print("\nGive me the name of a city and its country:")
    print("(enter 'q' to quit at any time)")

    cit_name = input("City name: ")
    if cit_name == 'q':
        break

    cun_name = input("Country name: ")
    if cun_name == 'q':
        break

    formatted_name = city_country(cit_name, cun_name)
    print(formatted_name)