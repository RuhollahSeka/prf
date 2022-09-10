from django.urls import path

from . import views

urlpatterns = [
    path('', views.VariantListAPIView.as_view(), name='products-list'),
    path('pallet-types/', views.PalletTypeListAPIView.as_view(), name='pallet-types-list'),
    path('shrink-wraps/', views.ShrinkWrapListAPIView.as_view(), name='shrink-wraps-list'),
    path('inventories/', views.BayInventoryEditAPIView.as_view(), name='inventories-edit'),
]
