from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerListAPIView.as_view(), name='customers-list'),
]
