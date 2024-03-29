from django.shortcuts import render, redirect
from main import models


def index(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    reviews = models.Review.objects.all()
    context = {
        'products':products,
        'categories':categories,
        'reviews':reviews,
    }
    return render(request, 'front/index.html', context)


