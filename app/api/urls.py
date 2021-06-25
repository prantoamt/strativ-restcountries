from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework import routers
from api.country.views import CountryViewSet
from api.language.views import LanguageViewSet

router = routers.DefaultRouter()

router.register(r'countries', CountryViewSet, 'countries')
router.register(r'languages', LanguageViewSet, 'languages')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
