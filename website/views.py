from django.shortcuts import render
from bookstore.models import Category,Author, Book
# Create your views here.


def home(request):
    context = dict()
    context['cats'] = Category.objects.all()
    context['books'] = Book.objects.all()
    return render(request, 'index.html',context)
