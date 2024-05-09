from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'uploads'
urlpatterns = [
    path('', views.index, name='index'),
    path('custom/<int:dataset_id>/', views.custom, name='custom'),
    # path("set_attr/<int:dataset_id>", views.set_attr, name="set_attr"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)