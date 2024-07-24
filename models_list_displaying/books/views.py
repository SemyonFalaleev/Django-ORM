from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {"books": books}
    return render(request, template, context)

def books_date_view(request, pub_date):
    template = 'books/books_list.html'
    pub_date_list = []
    books = Book.objects.all().order_by("pub_date")
    pub_date_dict = {}
    for book in books:
        pd = book.pub_date.strftime("%Y-%m-%d")
        if pub_date_dict.get(pd, False):
            pub_date_dict[pd].append(book)
            continue
        else:
            pub_date_dict[pd] = []
            pub_date_dict[pd].append(book)
    for i, key in enumerate(pub_date_dict):
        pub_date_list.append(key)
        if key == pub_date:
            index = i
    try:
        next_date = pub_date_list[index+1]
    except IndexError:
        next_date = None
    if index - 1 <= 0 :
        previous_date = None
    else:    
        previous_date = pub_date_list[index-1]
    page_objects = pub_date_dict[pub_date]
    print(page_objects)
    context ={
            "books" : page_objects,
            "next_date": next_date,
            'previous_date': previous_date,
    }
    return render(request, template, context)
