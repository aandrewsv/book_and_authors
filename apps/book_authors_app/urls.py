from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.books),
    path('books/<int:idn>', views.showbooks),
    path('authors', views.authors),
    path('authors/<int:idn>', views.showauthors),
    path('newbook', views.newbook),
    path('addbook/<int:idn>', views.addbook),
    path('newauthor', views.newauthor),
    path('addauthor/<int:idn>', views.addauthor),
    ]