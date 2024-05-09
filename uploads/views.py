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
    context['datasets'] = dataset.columns.tolist()
    return render(request, 'uploads/custom.html', context)

# def set_attr(request, dataset_id):
#     context = {'dataset_id': dataset_id}
#     if request.method == 'POST':
#         print(request.POST)
#         categorical = []
#         numerical = []

#         for key, value in request.POST.items():
#             if value == 'category':
#                 categorical.append(key)
#             elif value == 'numeric':
#                 numerical.append(key)


#         dataset = Dataset.objects.get(id=dataset_id)
#         dataset_filename = dataset.file
#         dataset_path = os.path.join(settings.MEDIA_ROOT, str(dataset_filename))
#         dataset = pd.read_csv(dataset_path)

#         dataset[categorical] = dataset[categorical].astype('category')

#         label = request.POST['label']
#         attr_label = dataset[label]
#         attr_features = dataset.drop(label, axis=1)
#     else:
#         return redirect('uploads:custom', dataset_id=dataset_id)
