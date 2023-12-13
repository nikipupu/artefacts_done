from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Products
from .forms import AddForm
from django.views import generic

class HomeView(generic.ListView):
    template_name="main/home.html"
    context_object_name="object_list"
    
    def get_queryset(self):
        return Products.objects.all()

def add_product(request):
    error = ""
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма неверна"
    form = AddForm()

    data = {
        'error': error,
        'form': form,
    }
    return render(request, 'main/add_product.html', data)
