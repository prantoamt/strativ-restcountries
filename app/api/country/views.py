from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import Serializer
from .serializers import CountrySerializer
from country.models import Country
from api.utils.content_object import Content


class CountryViewSet(viewsets.ModelViewSet):
    model = Country
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    lookup_field = 'uuid'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        kgus = {}
        if self.request.query_params.get('country_name', None):
            kgus['name__icontains'] = self.request.query_params.get('country_name')
        content = Content()
        content.set_countries(**kgus)
        data = content.get_data()
        return data

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, uuid):
        content = Content()
        content.set_selected_country_details(uuid)
        data = content.get_data()
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, uuid=None):
        data = request.data.copy()
        instance = get_object_or_404(Country, id=uuid)
        serializer = self.get_serializer(
            instance, data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, uuid=None):
        data = request.data.copy()
        instance = get_object_or_404(Country, id=uuid)
        serializer = self.get_serializer(
            instance, data=data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, uuid):
        try:
            instance = get_object_or_404(Country, id=uuid)
            self.perform_destroy(instance)
        except Exception as e:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
