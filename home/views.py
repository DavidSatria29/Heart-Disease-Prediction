from django.shortcuts import render
from django.shortcuts import redirect
from uploads.models import Dataset
# Create your views here.

def index(request):
    context = {}
    dataset = Dataset.objects.all()
    context['datasets'] = dataset
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'about/about.html')

def panduan(request):
    return render(request, 'panduan/panduan.html')

def prediksi(request):
    return render(request, 'prediksi/prediksi.html')

def contact(request):
    return render(request, 'contact/contact.html')

def list_dataset(request):
    context = {}
    dataset = Dataset.objects.all()
    context['datasets'] = dataset
    return render(request, 'home/listDataset.html', context)