from api.country.serializers import CountrySerializer
from country.models import Country, CountryLanguage, CountryNeighbour


class Content(object):

    def __init__(self) -> None:
        super().__init__()
        self.data = {}

    def set_countries(self, **kwargs) -> None:
        '''Sets all countries or queried country's 
        data in instance's data'''
        kgus = kwargs.copy()
        self.data = CountrySerializer(
            Country.objects.filter(**kgus), many=True).data

    def set_selected_country_details(self, uuid: str) -> None:
        '''Takes uuid of a country as an argument and sets the full details including
        it's languages and neighbours' name in instance's data'''
        country = Country.objects.filter(id=uuid).first()
        if country:
            self.data = CountrySerializer(country).data
            spoken_languages, neighbour_countries = self.__get_country_languages_and_neighbours(
                country, **{'spoken_languages': True, 'neighbour_countries': True})
            self.data['languages'] = spoken_languages
            self.data['neighbours'] = neighbour_countries

    def set_neighbour_countries_and_their_languages(self, uuid: str, **kwargs) -> None:
        '''Takes uuid of a specific country as an argument and sets it's neighbours and 
        their spoken languages in instance's data.
        If you want to get only the neighbouring countries of a country, 
        just pass only_neighbour_countries_list: True in **kwargs'''
        kgus = kwargs.copy()
        country_neighbours_qs = CountryNeighbour.objects.select_related('neighbour_country_id').filter(
            country_id__id=uuid)
        self.data = []
        # if kgus.get('only_neighbour_countries_list', None):
        #     self.data['neighbouring_countries'] = CountrySerializer(
        #         neighbour_countries.neighbour_country_id, many=True).data
        #     return
        for country in country_neighbours_qs:
            if kgus.get('only_neighbour_countries_list', None):
                self.data.append(CountrySerializer(
                country.neighbour_country_id).data)
                continue
            spoken_languages, neighbours = self.__get_country_languages_and_neighbours(
                country.neighbour_country_id, **{'spoken_languages': True})
            self.data[country.neighbour_country_id.name] = {
                'spoken_languages': spoken_languages}

    def __get_country_languages_and_neighbours(self, country :object, **kwargs) -> tuple:
        '''Takes country object and returns it's spoken languages and/or neighbours.
        This method is a helper method for other methods and scope should be protected,
        which means instances should not invoke it'''
        kgus = kwargs.copy()
        spoken_languages = None
        neighbour_countries = None
        if kgus.get('spoken_languages', None):
            spoken_languages = CountryLanguage.objects.filter(
                country_id=country).values_list('language_id__name', flat=True)
        if kgus.get('neighbour_countries', None):
            neighbour_countries = CountryNeighbour.objects.filter(
                country_id=country).values_list('neighbour_country_id__name', flat=True)
        return spoken_languages, neighbour_countries

    def get_data(self) -> dict:
        '''Return the content data that are setted so far'''
        return self.data
