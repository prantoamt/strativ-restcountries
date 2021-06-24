from django.urls import path, include
from rest_framework import routers
from api.country.views import CountryViewSet

router = routers.DefaultRouter()

router.register(r'countries', CountryViewSet, 'countries')


urlpatterns = [
    path('', include(router.urls)),
]
