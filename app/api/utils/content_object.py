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
        self.data['countries'] = CountrySerializer(
            Country.objects.filter(**kgus), many=True).data

    def set_selected_country_details(self, uuid :str) -> None:
        '''Takes uuid of a country as an argument and sets the full details including
        it's languages and neighbours' name in instance's data'''
        country = Country.objects.filter(id=uuid).first()
        if country:
            self.data['country_details'] = CountrySerializer(country).data
            spoken_languages, neighbour_countries = self.get_country_languages_and_neighbours(
                country, **{'spoken_languages': True, 'neighbour_countries': True})
            self.data['country_details']['languages'] = spoken_languages
            self.data['country_details']['neighbours'] = neighbour_countries

    def set_neighbour_countries_and_their_languages(self, uuid: str) -> None:
        '''Takes uuid of a specific country as an argument and sets it's neighbours' and 
        their spoken languages in instance's data'''
        neighbour_countries = CountryNeighbour.objects.filter(
            country_id__id=uuid).first().select_related('neighbour_country_id')
        for country in neighbour_countries:
            spoken_languages, neighbours = self.get_country_languages_and_neighbours(
                country.neighbour_country_id, **{'spoken_languages': True})
            self.data[country.neighbour_country_id.name] = {
                'spoken_languages': spoken_languages}

    def get_country_languages_and_neighbours(self, country, **kwargs):
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
        return self.data
