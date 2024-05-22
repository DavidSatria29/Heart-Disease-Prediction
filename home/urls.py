from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('panduan/', views.panduan, name='panduan'),
    path('prediksi/', views.prediksi, name='prediksi'),
    path('contact/', views.contact, name='contact'),
]