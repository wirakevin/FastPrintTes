from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def clean_nama_produk(self):
        nama = self.cleaned_data.get('nama_produk')
        if not nama:
            raise forms.ValidationError("Nama produk harus diisi")
        return nama

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga is None or harga <= 0:
            raise forms.ValidationError("Harga harus berupa angka lebih dari 0")
        return harga
