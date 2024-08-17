from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ProductModel , ProductStatusType
# Create your views here.
class ShopProductGridView(TemplateView):
    template_name = "shop/product-grid.html"
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)