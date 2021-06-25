from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from country.models import Language
from .serializers import LanguageSerializer
from api.utils.content_object import Content

class LanguageViewSet(viewsets.ModelViewSet):
    model = Language
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'
    http_method_names = ['get']

    def get_queryset(self):
        data = self.serializer_class(self.model.objects.all(), many=True).data
        return data
    
    @action(methods=['get'], detail=True, url_path='countries')
    def countries(self, request, uuid):
        content = Content()
        kgus = {
            'country_languages__language_id__id': uuid
        }
        content.set_countries(**kgus)
        data = content.get_data()
        return Response(data, status=status.HTTP_200_OK)