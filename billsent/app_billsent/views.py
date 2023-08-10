from django.shortcuts import render
from .models import Billsent

def index(request):
    billsent = Billsent.objects.all()
    context = {'billsent': billsent}
    return render(request, 'index.html')

def top_sellers(request):
    return render (request, 'top-sellers.html')