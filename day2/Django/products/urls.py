#from django.urls import re_path
#from django.views.generic.list import ListView

from django.urls import path

#from .views import BookDetailView, BookListView
from .views import book_list


urlpatterns = [
   # path("books", BookListView.as_view(), name="book-list"),
   # path("books/<int:pk>", BookDetailView.as_view(), name="book-detail")
   path("books", book_list, name="book_list"),
]
