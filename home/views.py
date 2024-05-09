from django.shortcuts import render
from django.shortcuts import redirect
from uploads.models import Dataset
# Create your views here.

def index(request):
    context = {}
    dataset = Dataset.objects.all()
    context['datasets'] = dataset
    return render(request, 'home/index.html', context)