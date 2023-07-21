#from django.urls import re_path
#from django.views.generic.list import ListView

from django.urls import path

#from .views import BookDetailView, BookListView
from .views import book_list, book_detail


urlpatterns = [
   # path("books", BookListView.as_view(), name="book-list"),  #.as_view() -> html형태로 보냄
   # path("books/<int:pk>", BookDetailView.as_view(), name="book-detail")
   path("books", book_list, name="book_list"),   #json으로 받을거야
   path("books/<int:pk>", book_detail, name="book-detail")
]
