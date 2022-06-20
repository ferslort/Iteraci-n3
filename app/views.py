from django.shortcuts import render, redirect
from django.contrib import messages

from .models import UserCustom, Supplier

from app.forms import FormLogin, FomRegister
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def page_index(request):
    return render(request, 'index.html')


def page_user(request):

    users = UserCustom.objects.all()

    return render(request, 'users.html', {
        'users': users
    })


def page_registerSupplier(request):

    if request.method == 'POST':

        razon = request.POST['razon']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']

        supplier = Supplier(
            razon=razon,
            address=address,
            phone=phone,
            email=email
        )

        supplier.save()

    return render(request, 'register.html')


def register_page(request):

    form = FomRegister()
    if request.method == 'POST':
        form = FomRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {
        'form': form
    })


def page_login(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('index')
        else:
            messages.warning(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html', {
        'form': form,
    })


def logout_user(request):
    logout(request)
    return redirect('index')
