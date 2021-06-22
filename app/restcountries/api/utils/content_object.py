from api.country.serializers import CountrySerializer
from country.models import Country, CountryLanguage, CountryNeighbour


class Content(object):

    def __init__(self) -> None:
        super().__init__()
        self.data = {}

    def set_countries(self, **kwargs) -> None:
        kgus = kwargs.copy()
        self.data['countries'] = CountrySerializer(
            Country.objects.filter(**kgus), many=True).data

    def set_country_details(self, **kwargs):
        country = Country.objects.filter(**kwargs).first()
        if country:
            self.data['country'] = CountrySerializer(country).data
            spoken_languages = CountryLanguage.objects.filter(
                country_id=country).values_list('language_id__name', flat=True)
            neighbour_countries = CountryNeighbour.objects.filter(
                country_id=country).values_list('neighbour_country_id__name', flat=True)
            self.data['country']['languages'] = spoken_languages
            self.data['country']['neighbours'] = neighbour_countries

    def get_data(self) -> dict:
        return self.data
