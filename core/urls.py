from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowMessages.as_view(), name='main'),
]