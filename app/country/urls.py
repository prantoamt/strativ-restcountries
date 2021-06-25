from django.urls import path
from .import views 

app_name = 'country'

urlpatterns = [
    path('', views.CountryListView.as_view(), name='countries'),
    path('<uuid:pk>/', views.CountryDetailView.as_view(), name='country_detail')
]