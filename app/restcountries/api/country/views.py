from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CountrySerializer
from country.models import Country
from api.utils.content_object import Content


class CountryViewSet(viewsets.ModelViewSet):
    model = Country
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    lookup_field = 'uuid'
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_queryset(self, *args, **kwargs):
        content = Content()
        content.set_countries(**kwargs)
        data = content.get_data()
        return data

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, uuid):
        content = Content()
        content.set_country_details(**{'id': uuid})
        data = content.get_data()
        return Response(data, status=status.HTTP_200_OK)
