from django.shortcuts import render
from .models import Billsent
from .forms import AdvertisementForm

def index(request):
    billsents = Billsent.objects.all()
    context = {'billsent': billsent}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render (request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            billsents = Advertisement(**form.cleaned_data)
            billsents.user = request.user
            billsents.save()
            return redirect(reverse('main-page'))
        form = AdvertisementForm()
        context = {'form': form}
        return render(request, 'advertisement-post.html', context)



    form = AdvertisementForm
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)
