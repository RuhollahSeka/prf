from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/customers/', include('customers.api.v1.urls')),
    path('api/v1/products/', include('products.api.v1.urls')),
    path('api/v1/requests/', include('requests.api.v1.urls')),
]
