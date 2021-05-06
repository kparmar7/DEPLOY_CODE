from django.shortcuts import render
from .models import Product

def list(req):
    q = Product.objects.all()
    return render(req, 'home.html', {'q':q})

