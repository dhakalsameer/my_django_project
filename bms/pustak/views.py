from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.models import User
from django.contrib import messages

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
        bn = request.POST.get('book_name')
        bd = request.POST.get('book_description')
        bi = request.FILES.get('book_image')
        update_book.book_name = bn
        update_book.book_description = bd
        if bi:
            update_book.book_image = bi
        update_book.save()
        return redirect('/')
    context = {'book': update_book}
    return render(request, 'pustak/updatebooks.html', context)

def login_page(request):
    
    return render(request, 'pustak/login.html')

def register_page(request):
    if request.method == 'POST':
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if not fn or not ln or not un or not pw:
            messages.error(request, 'All fields are required.')
            return redirect('/register')
        if User.objects.filter(username=un).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/register')
        User.objects.create_user(first_name=fn, last_name=ln, username=un, password=pw)
        messages.success(request, 'User registered successfully.')
        return redirect('/login')
    return render(request, 'pustak/register.html')

def logout_page(request):
    pass