from django.contrib import admin
from .models import Country, Language, CountryLanguage, CountryNeighbour
# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_editable = ['is_active']


admin.site.register(Country, CountryAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Language, LanguageAdmin)


class CountryLanguageAdmin(admin.ModelAdmin):
    list_display = ['country_id', 'language_id']


admin.site.register(CountryLanguage, CountryLanguageAdmin)


class CountryNeighbourAdmin(admin.ModelAdmin):
    list_display = ['country_id', 'neighbour_country_id']


admin.site.register(CountryNeighbour, CountryNeighbourAdmin)
