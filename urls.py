from django.urls import path, include 



urlpatterns = [
  path('', include('sw_shop.sw_customer.api.urls')),  
  path('api/', include('sw_shop.sw_customer.api.urls')),  
]
