from django.db.models.fields import related
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegistrationForm

from .forms import *
from .models import *


def home_page(request):
    byke = Byke.objects.all()
    category = Category.objects.all()
    scooter = Scooter.objects.all()
    image = Img.objects.all()

    context = {
        "byke": byke,
        "category": category,
        "scooter": scooter,
        "image": image,

    }
    return render(request, 'base.html', context)




def item_page_byke(request, slug_id, ):
    byke = Byke.objects.exclude(slug=slug_id)
    category = Category.objects.all()
    # categories = get_object_or_404(, slug=slug_category)
    items = get_object_or_404(Byke, slug=slug_id)
    
    context = {
        "byke": byke,
        "category": category,
        "items": items,
        # "categories": categories,
    }
    return render(request, 'shop_pages/shop_item_byke.html', context)





def item_page_scooter(request, slug_pk):
    scooter = Scooter.objects.exclude(slug=slug_pk)
    category = Category.objects.all()
    # categories = get_object_or_404(Scooter, slug_cat=slug_category)
    items = get_object_or_404(Scooter, slug=slug_pk)

    context = {
        "category": category,
        "scooter": scooter,
        "items": items,
    }

    return render(request, 'shop_pages/shop_item_scooter.html', context)


def add_item_byke(request):

    if request.method == "POST":
        form = AddBykeForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddBykeForm()

    context = {
        'form': form
    }

    return render(request, 'add_item_byke.html', context)


def add_item_scooter(request):

    if request.method == "POST":
        form = AddScooterForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddScooterForm()

    context = {
        'form': form
    }

    return render(request, 'add_item_scooter.html', context)



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'base.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})