from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from adminpage.models import Stock
from django_filters.views import FilterView
import time
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import make_aware
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def landing(request):
    return render(request, 'landing.html')
    

class ProductView(FilterView):
    def get(self, request):
        order_by = request.GET.get('order_by')
        direction = request.GET.get('direction')
        search = request.GET.get('search')
        if order_by:
            ordering = order_by
        else:
            ordering = "name"
        if direction == 'desc':
            ordering = '-{}'.format(ordering)
        if search:
            queryset = Stock.objects.filter(name__icontains=search).order_by(ordering)
        else:
            queryset = Stock.objects.all().order_by(ordering)
        paginator = Paginator(queryset, 10)
        page = request.GET.get('page')
        try:
            all_stock = paginator.page(page)
        except PageNotAnInteger:
            all_stock = paginator.page(1)
        except EmptyPage:
            all_stock = paginator.page(paginator.num_pages)
        return render(request, 'product.html',{'all_stock': all_stock, 'order_by': order_by, 'direction': direction, 'search': search})


def ProductDetailView(request, pk):
    product = Stock.objects.get(pk=pk)
    is_del = Stock.objects.filter(pk=pk).values_list("is_deleted", flat=True)[0]
    if is_del:
        return redirect('product')
    else:
        context = {"product":product, "title":'Detail Produk'}
        return render(request, "product_detail.html", context=context)

