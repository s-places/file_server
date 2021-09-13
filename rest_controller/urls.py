from django.urls import path
from . import views

urlpatterns = [
    path('', views.RetrieveFilesView.as_view(), name='root'),
    path('file/<int:pk>', views.RetrieveFileView.as_view(), name='file'),
    path('files/', views.RetrieveFilesView.as_view(), name='file'),
    path('send/', views.CreateFileView.as_view(), name='send'),
]
