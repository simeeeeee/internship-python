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

def book_detail(request, pk):
    try:
        book = Book.objects.get(pk = pk)  #특정 Book object를 가져온다
        data = {
            "book" : {
                "author": book.author.name,
                "name": book.name,
                "description": book.description,
                "shipping_cost": book.shipping_cost,
                "quantity": book.quantity
            }
        }
        response = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
        return response
    except Book.DoesNotExist:
        print("Book object doesn't exist")
        return None
    ## 원래는 없는 경우에 대비해서 try / except Book.DoesnotExist  등 처리를 해줘야 함
    
    """
    과제 (24일 오후 11시)
    1. 구현하지 못한 try/except 를 구현하거나
    2. model 에 좀 더 추가해서 조금 더 다채롭게 만들어보거나
    3. ppt를 보고 ChatGPT API를 사용해서 뭔가를 만들어보거나
    4. Codespace 로 배포해보기
    """