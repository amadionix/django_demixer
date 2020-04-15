from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('select2/', views.select2, name='select2'),
    path('select4/', views.select4, name='select4'),

    path('select2/process2', views.process2, name='process2'),
    path('select4/process4', views.process4, name='process4'),

    path('select2/download/', views.download, name='download'),
    path('select4/download/', views.download, name='download'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)