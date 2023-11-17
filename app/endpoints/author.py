from rest_framework import serializers
from rest_framework import viewsets

from app import models


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Author
    fields = '__all__'


class AuthorViewSet(viewsets.ModelViewSet):
  queryset = models.Author.objects.all()
  serializer_class = AuthorSerializer