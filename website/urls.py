
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.BooksListView.as_view(), name='home'),
    url(r'^cat/(?P<cat_id>[0-9]+)$', views.BooksListView.as_view(), name='cat'),
    url(r'^book/(?P<pk>[0-9]+)$', views.BookDetailView.as_view(), name='book-detail'),
]
