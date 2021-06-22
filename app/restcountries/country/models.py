from django.db import models
import uuid
# Create your models here.


class Country(models.Model):
    id = models.UUIDField(db_column='country_id', verbose_name='Country ID',
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, verbose_name='Name')
    alphacode_2 = models.CharField(max_length=256, verbose_name='Alpha Code 2')
    capital = models.CharField(max_length=256, verbose_name='Capital')
    population = models.IntegerField(verbose_name='Population')
    timezone = models.CharField(max_length=256, verbose_name='Timezone')
    flag = models.CharField(max_length=256, verbose_name='Flag')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name_plural = '1. Countries'
        db_table = 'Country'

    def __str__(self) -> str:
        return self.name


class Language(models.Model):
    id = models.UUIDField(db_column='language_id', verbose_name='Language ID',
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, verbose_name='Name', unique=True)

    class Meta:
        verbose_name_plural = '2. Languages'
        db_table = 'Language'

    def __str__(self) -> str:
        return self.name


class CountryLanguage(models.Model):
    id = models.UUIDField(db_column='country_language_id', verbose_name='Country Language ID',
                          primary_key=True, default=uuid.uuid4, editable=False)
    country_id = models.ForeignKey(
        'country.Country', on_delete=models.CASCADE, verbose_name='Country ID', related_name='country_languages')
    language_id = models.ForeignKey(
        'country.Language', on_delete=models.CASCADE, verbose_name='Language ID', related_name='countries')

    class Meta:
        verbose_name_plural = '3. Country Languages'
        db_table = 'CountryLanguage'

    def __str__(self) -> str:
        return self.country_id.name


class CountryNeighbour(models.Model):
    id = models.UUIDField(db_column='country_neighbour_id', verbose_name='Country Neighbour ID',
                          primary_key=True, default=uuid.uuid4, editable=False)
    country_id = models.ForeignKey(
        'country.Country', on_delete=models.CASCADE, verbose_name='Country ID', related_name='country_of_neighbour_country')
    neighbour_country_id = models.ForeignKey(
        'country.Country', on_delete=models.CASCADE, verbose_name='Neighbour Country ID', related_name='neighbour_country_of_country')

    class Meta:
        verbose_name_plural = '4. Country Neighbours'
        db_table = 'CountryNeighbour'

    def __str__(self) -> str:
        return self.country_id.name
