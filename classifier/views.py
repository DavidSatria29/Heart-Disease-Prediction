import os
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from uploads.models import Dataset
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import graphviz
from sklearn import tree
from .models import Model
import joblib


# Create your views here

def model(request, dataset_id):
    model = Model()
    context = {'dataset_id': dataset_id}
    dataset = Dataset.objects.get(id=dataset_id)
    dataset_title = dataset.title

    if request.method == 'POST':
        categorical = []
        numerical = []

        for key, value in request.POST.items():
            if value == 'category':
                categorical.append(key)
            elif value == 'numeric':
                numerical.append(key)

        # Load dataset
        dataset = Dataset.objects.get(id=dataset_id)
        dataset_filename = dataset.file
        dataset_path = os.path.join(settings.MEDIA_ROOT, str(dataset_filename))

        # Preprocess dataset
        dataset = pd.read_csv(dataset_path)

        # Convert categorical data type
        dataset[categorical] = dataset[categorical].astype('category')

        # set label and features
        label = request.POST['label']
        attr_label = dataset[label]
        attr_features = dataset.drop(label, axis=1)

        # get parameters for model
        parameters = {
            'criterion': request.POST['criterion'],
            'max_depth': int(request.POST['max_depth']),
            'min_samples_split': int(request.POST['min_samples_split']),
            'min_samples_leaf': int(request.POST['min_samples_leaf'])
        }
        # Train model
        kf = KFold(n_splits=10)
        performances = []
        models = []
        report_list = []
        for train_index, test_index in kf.split(attr_features):
            X_train, X_test = attr_features.iloc[train_index], attr_features.iloc[test_index]
            y_train, y_test = attr_label.iloc[train_index], attr_label.iloc[test_index]
            # Latih model
            clf = DecisionTreeClassifier(**parameters)
            clf.fit(X_train, y_train)
            
            # Evaluasi model
            accuracy = clf.score(X_test, y_test)
            y_pred = clf.predict(X_test)
            report_model = classification_report(y_test, y_pred, output_dict=True, zero_division=1)

            # Simpan model dan performanya
            models.append(clf)
            performances.append(accuracy)
            report_list.append(report_model)

        # Pilih model terbaik
        best_model_index = performances.index(max(performances))
        report_metrics = report_list[best_model_index]
        best_model = models[best_model_index]

        class_name = list(best_model.classes_)
        class_name = [str(i) for i in class_name]
        # Simpan model ke dalam file
        file_path = f'models/{dataset_title}.joblib'
        file_source = f'image/{dataset_title}'
        joblib.dump(best_model, 'media/'+ file_path)
        dot_data = tree.export_graphviz(best_model, out_file=None, filled=True, rounded=True, special_characters=True, feature_names=attr_features.columns, class_names=class_name)
        graph = graphviz.Source(dot_data)
        graph.render('media/'+ file_source, format='pdf')

        # Simpan model ke dalam database
        model.title = dataset_title
        model.file = file_path
        model.label = label
        model.image = file_source + '.pdf'
        model.save()

        # show 10 data in dataset
        show = dataset.head(10)
        # deploy to view
        context['show'] = show.to_html(index=False)
        context['label'] = label
        context['performances'] = report_metrics
        return render(request, 'classifier/model.html', context)
    else:
        dataset = Dataset.objects.get(id=dataset_id)
        dataset_title = dataset.title
        dataset_path = os.path.join(settings.MEDIA_ROOT, str(dataset.file))
        dataset = pd.read_csv(dataset_path)
        show = dataset.head(10)
        model_title = Model.objects.get(title=dataset_title)
        model_image = model_title.image
        model_label = model_title.label
        model_image = model_title.image
        context['show'] = show.to_html(index=False)
        context['label'] = model_label
<<<<<<< HEAD
        context['image'] = model_title.image
=======
        context['image'] = model_image
>>>>>>> 14520758059e59c9581aeb020b4bbc3460d5f2f1
        return render(request, 'classifier/model.html', context)
    
    
    

    
def predict(request, dataset_id):
    context = {'dataset_id': dataset_id}
    if request.method == 'POST':
        label = request.POST['label']
        dataset = Dataset.objects.get(id=dataset_id)
        dataset_name = dataset.title
        dataset_filename = dataset.file
        dataset_path = os.path.join(settings.MEDIA_ROOT, str(dataset_filename))
        dataset = pd.read_csv(dataset_path)
        feature = dataset.drop(label, axis=1)
        feature = feature.columns.tolist()
        context['features'] = feature
        return render(request, 'classifier/predict.html', context)
    else:
        return redirect('classifier:model', dataset_id=dataset_id)

def result(request, dataset_id):
    context = {'dataset_id': dataset_id}
    dataset = Dataset.objects.get(id=dataset_id)
    dataset_name = dataset.title
    dataset_filename = dataset.file
    dataset_path = os.path.join(settings.MEDIA_ROOT, str(dataset_filename))
    dataset = pd.read_csv(dataset_path)


    model = Model.objects.get(title=dataset_name)
    models_file = model.file
    models_path = os.path.join(settings.MEDIA_ROOT, str(models_file))
    model_joblib = joblib.load(models_path)

    if request.method == 'POST':
        attr = []
        values = []
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken':
                continue
            attr.append(key)
            values.append(value)
        
        data = pd.DataFrame([values], columns=attr)
        prediction = model_joblib.predict(data)
        print(prediction[0])
        context['prediction'] = prediction[0]
        return render(request, 'classifier/result.html', context)
    else:
        return redirect('classifier:predict', dataset_id=dataset_id)