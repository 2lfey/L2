from rest_framework import routers

from . import book
from . import author


router = routers.DefaultRouter()

router.register('books', book.BookViewSet)
router.register('authors', author.AuthorViewSet)
