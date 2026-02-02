from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk
from .forms import ProdukForm
from .get_produk import get_data

def daftar_produk(request):
    produk_list = Produk.objects.all()
    get_data()
    return render(request, 'produk/daftar_produk.html', {'produk_list': produk_list})

def produk_bisa_dijual(request):
    produk_list = Produk.objects.filter(status__nama_status__iexact="bisa dijual")
    return render(request, 'produk/daftar_produk.html', {'produk_list': produk_list})

def tambah_produk(request):
    if request.method == "POST":
        form = ProdukForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('daftar_produk')
    else:
        form = ProdukForm()
    return render(request, 'produk/form_produk.html', {'form': form})

def edit_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == "POST":
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('daftar_produk')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/form_produk.html', {'form': form})

def hapus_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == "POST":
        produk.delete()
        return redirect('daftar_produk')
    return render(request, 'produk/konfirmasi_hapus.html', {'produk': produk})
