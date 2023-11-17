from django.urls import path, include

from .endpoints import router

from . import views


urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('api/', include(router.urls)),
  path('books/<int:pk>/', views.BookView.as_view(), name='book'),
] 