from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import ProductModel, ProductStatusType,ProductCategoryModel

# Create your views here.
class ShopProductGridView(ListView):
    template_name = "shop/product-grid.html"
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)
    paginate_by = 9  # Use paginate_by instead of paginate for ListView

    def get_queryset(self):
        queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)
        
        if search_q:=self.request.GET.get("q"):
             queryset=queryset.filter(title__icontains =search_q)
        if category_id:=self.request.GET.get("category"):
             queryset=queryset.filter(category_id =category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        context['categories'] = ProductCategoryModel.objects.all()

        return context

class ShopProductDetailView(DeleteView):
    template_name = "shop/product-detail.html"
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)
