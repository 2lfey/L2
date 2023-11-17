from rest_framework import serializers, viewsets, filters

from app import models


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Author
    fields = '__all__'


class AuthorViewSet(viewsets.ModelViewSet):
  queryset = models.Author.objects.all()
  serializer_class = AuthorSerializer
  filter_backends = [filters.SearchFilter]