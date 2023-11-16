from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic as generic_views

from . import models


class IndexView(generic_views.ListView):
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return models.Book.objects.all()


class BookView(generic_views.DetailView):
    template_name = 'detail.html'
    context_object_name = 'book'
    model = models.Book
