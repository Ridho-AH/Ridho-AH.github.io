from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
import time
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import make_aware
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StockListView(FilterView):
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
        return render(request, 'stock.html',{'all_stock': all_stock, 'order_by': order_by, 'direction': direction, 'search': search})


# class StockCreateView(SuccessMessageMixin, CreateView):
    # model = Stock
    # form_class = StockForm
    # template_name = "stock_edit.html"
    # success_url = '/stock'
    # success_message = "Stok berhasil ditambahkan"

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["title"] = 'Tambah Stok Baru'
        # context["savebtn"] = 'Tambahkan Stok'
        # return context       

def StockCreateView(request):
    form = StockForm()
    if request.method == "POST":
        form = StockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Stok berhasil ditambahkan")
            return redirect('stock')
        else:
            form = StockForm()
    context = {"form":form, "title":'Tambah Stok Baru', "savebtn":'Tambahkan Stok'}
    return render(request, "stock_edit.html", context=context)


def StockEditView(request, pk):
    post = Stock.objects.get(pk=pk)
    form = StockForm(instance=post)
    if request.method == "POST":
        form = StockForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Informasi stok berhasil diubah")
            return redirect('stock')
        else:
            form = StockForm()
    context = {"form":form, "object":post, "title":'Ubah Informasi Stok', "savebtn":'Ubah Informasi', "delbtn":'Hapus Stok'}
    return render(request, "stock_edit.html", context=context)


# class StockEditView(SuccessMessageMixin, UpdateView):
    # model = Stock
    # form_class = StockForm
    # template_name = "stock_edit.html"
    # success_url = '/stock'
    # success_message = "Informasi stok berhasil diubah"

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["title"] = 'Ubah Informasi Stok'
        # context["savebtn"] = 'Ubah Informasi'
        # context["delbtn"] = 'Hapus Stok'
        # return context


# class StockDeleteView(View):
    # template_name = "stock_delete.html"
    # success_message = "Stok berhasil dihapus"
    
    # def get(self, request, pk):
        # stock = get_object_or_404(Stock, pk=pk)
        # return render(request, self.template_name, {'object' : stock})

    # def post(self, request, pk):  
        # stock = get_object_or_404(Stock, pk=pk)
        # stock.is_deleted = True
        # stock.save()                                               
        # messages.success(request, self.success_message)
        # return redirect('stock')


class StockDeleteView(View):
    template_name = "stock_delete.html"
    success_message = "Stok berhasil dihapus"
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock= Stock.objects.get(pk=pk)
        stock.delete()                                 
        messages.success(request, self.success_message)
        return redirect('stock')

class GuideView(TemplateView):
    template_name = "guide.html"

