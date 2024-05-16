import pandas as pd
import os
from django.shortcuts import render
from django.shortcuts import redirect
from . forms import UploadFileForm
from . models import Dataset
from django.conf import settings
from sklearn.model_selection import KFold

# Create your views here.
def index(request):
    context = {'form': UploadFileForm()}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        dataset_id = form.instance.id
        return redirect('uploads:custom', dataset_id=dataset_id)
    else:
        return render(request, 'uploads/index.html', context)
    # return render(request, 'uploads/index.html', context)

def custom(request, dataset_id):
    context = {'dataset_id': dataset_id}
    dataset = Dataset.objects.get(id=dataset_id)
    dataset_filename = dataset.file
    dataset_path = os.path.join(settings.MEDIA_ROOT, str(dataset_filename))
    dataset = pd.read_csv(dataset_path)
    show = dataset.head(10)
    context['datasets'] = dataset.columns.tolist()
    context['show'] = show.to_html(index=False)
    return render(request, 'uploads/custom.html', context)

