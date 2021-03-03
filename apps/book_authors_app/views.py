from django.shortcuts import redirect, render, HttpResponse
from .models import *

# Create your views here.
def books(request):
    context ={
        "all_books": book.objects.all()
    }
    return render(request,"books.html", context)

def showbooks(request, idn):
    this_book = book.objects.get(id=idn)
    context ={
        "book": this_book,
        "book_authors": this_book.authors.all(),
        "all_authors": author.objects.all(),
    }
    return render(request, "showbook.html", context)

def newbook(request):
    book.objects.create(title=f"{request.POST['title']}", desc=f"{request.POST['desc']}")
    return redirect("/")

def addauthor(request, idn):
    this_book=book.objects.get(id=idn)
    selected_author = author.objects.get(id=request.POST['selectauthor'])
    this_book.authors.add(selected_author)
    return redirect(f"/books/{idn}")

def authors(request):
    context ={
        "all_authors": author.objects.all()
    }
    return render(request, "authors.html", context)

def showauthors(request, idn):
    this_author = author.objects.get(id=idn)
    context ={
        "author": this_author,
        "author_books": this_author.books.all(),
        "all_books": book.objects.all(),
    }
    return render(request, "showauthor.html", context)

def newauthor(request):
    author.objects.create(first_name=f"{request.POST['fname']}", last_name=f"{request.POST['lname']}", notes=f"{request.POST['notes']}")
    return redirect("/authors")

def addbook(request, idn):
    this_author=author.objects.get(id=idn)
    selected_book=book.objects.get(id=request.POST['selectbook'])
    this_author.books.add(selected_book)
    return redirect(f"/authors/{idn}")
