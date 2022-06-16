from django.shortcuts import render

from .models import UserCustom, Supplier

from app.forms import FormSupplier

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

    return render(request, 'register_supplier.html')
