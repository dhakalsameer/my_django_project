from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def book(request):
    if request.method == 'POST':
        bm = request.POST.get('book_name')
        bd = request.POST.get('book_description')
        bi = request.FILES['book_image']
        Book.objects.create(book_name=bm, book_description=bd, book_image=bi)
        return redirect('/')
    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request,'pustak/books.html', context)

def delete_book(request, id):
    delete_book = Book.objects.get(id=id)
    delete_book.delete()
    return redirect('/')

def update_book(request, id):
    update_book = Book.objects.get(id=id)
    if request.method == 'POST':
        update_book.book_name = request.POST.get('book_name')
        update_book.book_description = request.POST.get('book_description')
        update_book.book_image = request.FILES.get('book_image',update_book.book_image)
        update_book.save()
        return redirect('/')
    context = {'book': update_book}
    return render(request, 'pustak/updatebooks.html', context)
