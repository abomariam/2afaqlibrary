from django.shortcuts import render
from bookstore.models import Category,Author, Book
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
# Create your views here.


class BooksListView(ListView):
    template_name = 'index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(BooksListView, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        if 'cat_id' in self.kwargs:
            cat = get_object_or_404(Category, pk=self.kwargs['cat_id'])
            qs = cat.books.all()
        else:
            qs= Book.objects.all()

        if 'q' in self.request.GET:
            q = self.request.GET['q']
            qs = qs.filter(Q(title__icontains=q) | Q(author__name__icontains=q)).distinct()
        return qs


class BookDetailView(DetailView):
    model = Book