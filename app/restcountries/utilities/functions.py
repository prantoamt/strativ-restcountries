import requests
from country.models import Country, Language, CountryLanguage, CountryNeighbour


def create_and_map_language(country: object, languages: list) -> None:
    '''Takes a country objects and a list of languages it speaks.
    Steps of operations:
        1. The function pops and takes the last item from the languages list.
        2. Creates the popped Language's entry in Language table if Language with this name does not exist.
        3. Maps the country with the newly created language by creating a new entry in CountryLanguage Table.
        4. Invokes itself recursively until the languages list becomes empty.'''
    if len(languages) == 0:
        return
    else:
        language = languages.pop()
        language_obj, created = Language.objects.get_or_create(
            name=language.get('name'))
        if created:
            CountryLanguage.objects.get_or_create(
                country_id=country, language_id=language_obj)
        create_and_map_language(country, languages)


def create_and_map_neighbouring_country(data: list, country: object, neighbours: list) -> list:
    '''Takes data(list of dicts or list of JSON objects of countries), Country object and a list of its neighbours(alpha3Codes). 
    After execution, returns the updated data(list of dicts or list of JSON objects of countries)
    Steps of operations:
        1. The function pops and takes the last item from neighbours list.
        2. Iterates through the data until an alpha3Code of a country is matched with the popped item.
        3. Once matched, creates a new country(neighbour country) in Country Table if does not exist.
        4. Creates new Languages which are spoken by the newly created Country.
        5. Maps this country(neighbour country) with the given country by creating new entry in CountryNeighbour Table.
        6. Removes the country which is newly created at step 3 from the data list so that unneccessary iterations can be inhibited.
        7. Invokes iteself recursively until the neighbours list becomes empty. During recursion, it sends the
            updated data list in the argument.
        8. Finally returns the updated data list.'''
    if len(neighbours) == 0:
        return data
    else:
        neighbour = neighbours.pop()
        for item in data:
            if item.get('alpha3Code', 'None') == neighbour:
                neighbour_country, created = Country.objects.get_or_create(name=item.get('name'), alphacode_2=item.get('alpha2Code'), capital=item.get(
                    'capital'), population=item.get('population'), timezone=item.get('timezones')[0], flag=item.get('flag'))
                if created:
                    create_and_map_language(
                        neighbour_country, item.get('languages', []))

                    CountryNeighbour.objects.get_or_create(
                        country_id=country, neighbour_country_id=neighbour_country)
                    data.remove(item)
                    break
    return create_and_map_neighbouring_country(data, country, neighbours)


def get_data() -> None:
    '''Steps of operations:
        1. The function fetches all countries from the url.
        2. Iterate through each country and creates new entry in Country table.
        3. Creates Languages that are spoken by the newly created country.
        4. Creates and maps the neighbouring countries with the newly created countries.'''
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    data = response.json()
    for item in data:
        country, created = Country.objects.get_or_create(name=item.get('name'), alphacode_2=item.get('alpha2Code'), capital=item.get(
            'capital'), population=item.get('population'), timezone=item.get('timezones')[0], flag=item.get('flag'))
        if created:
            create_and_map_language(country, item.get('languages', []))
            data = create_and_map_neighbouring_country(
                data, country, item.get('borders', []))
