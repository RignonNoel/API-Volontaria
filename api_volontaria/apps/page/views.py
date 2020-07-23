from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from api_volontaria.apps.page.serializers import (
    PageSerializer,
)
from .models import (
     Page,
)


class PageViewSet(viewsets.ModelViewSet):

    serializer_class = PageSerializer
    queryset = Page.objects.all()
    filterset_fields = '__all__'
    permission_classes = [IsAdminUser]
