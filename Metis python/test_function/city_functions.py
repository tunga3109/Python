#стр 229 упр 11.1

def county_city(country, city, population=''):
    if population:
        country_and_city = f'{country},{city} - Population {population}'
    else:
        country_and_city = f'{country},{city}'
    return country_and_city.title()
