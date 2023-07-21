# #template sample -> 데이터를 출력하는 역할

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from .models import Author, Book   # .models ->현재 위치와 같은 위치의 modelsdptj author, book가져와

# #데이터를 받을 경로 설정 -> product/urls.py
# class BookListView(ListView):
#     model = Book
#     template_name = "book_list.html"

# class BookDetailView(DetailView):
#     model = Book
#     template_name = "book_detail.html"

from django.http import JsonResponse
from .models import Book, Author


def book_list(request):
    print('request를 받았다')
    books = Book.objects.all()  #장고내 ORM Book object를 다 가져온다
    data = {"books": list(books.values())}  ##dict
    #response = JsonResponse(data)  #dict를 json화 시켜준다
    #return response
    response = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return response
