from rest_framework import serializers, viewsets, response

from app import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        searchBy = request.query_params['searchBy']
        query = request.query_params['query']
        
        if searchBy and query:
            queryset = self.queryset.filter(**{searchBy: query})
            serializer = self.get_serializer(queryset, many=True)
            return response.Response(serializer.data)

        return super().list(request, *args, **kwargs)