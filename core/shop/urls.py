from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path("product/list/",views.ShopProductListView.as_view(),name='product-list'),

    ]