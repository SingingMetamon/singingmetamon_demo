from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='main'),
    # path('test/', views.test, name='test'),
]