from django.shortcuts import render
from bookstore.models import Category,Author, Book
from django.db.models import Q
# Create your views here.


def home(request):
    context = dict()
    context['cats'] = Category.objects.all()
    qs = Book.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        qs = qs.filter(Q(title__icontains=q)|Q(author__name__icontains=q)).distinct()
    context['books'] = qs
    return render(request, 'index.html',context)
