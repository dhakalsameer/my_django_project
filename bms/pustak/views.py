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
