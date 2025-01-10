from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

from aptanimelistweb.models import List
from .forms import registerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import List
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registerForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ganti 'home' dengan nama URL halaman utama Anda
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    list = List.objects.all()
    return render(request,'aptanimelistweb/home.html',{
        'list' : list,
       

    })


def search(request):
    query = request.GET.get('q')
    if query:
        results = List.objects.filter(judul__icontains=query)
    else:
        results = List.objects.all()

    return render(request, 'aptanimelistweb/search.html', {'results': results, 'query': query})


def populer(request):
    populer_list = List.objects.all()[:9]
    return render(request,'aptanimelistweb/populer.html',{
        'populer_list' : populer_list,
       

    })
