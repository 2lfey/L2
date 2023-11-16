from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('books/<int:pk>/', views.BookView.as_view(), name='book'),
] 