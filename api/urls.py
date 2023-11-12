from django.urls import path
from .views import FilteredProductsView

urlpatterns = [
    path('filtered-products/', FilteredProductsView.as_view(), name='filtered-products'),
]
