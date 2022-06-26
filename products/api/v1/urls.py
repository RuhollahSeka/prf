from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='products-list'),
]
