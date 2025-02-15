from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        # photo = forms.ImageField()
        # self.fields['description'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        # self.fields['discount'].widget.attrs.update({'class': 'textinput form-control', 'min': '0', 'max': '100'})

    class Meta:
        model = Stock
        fields = ['name', 'photo', 'description', 'price', 'discount']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}), 
            'photo': forms.FileInput(attrs={"class": "form-control"}),
            'description': forms.TextInput(attrs={"class": "form-control"}), 
            'price': forms.TextInput(attrs={"class": "form-control", "min": "0"}), 
            'discount': forms.TextInput(attrs={"class": "form-control", "min": "0", "max": "100"}),
        }
        labels = {
			'name': ('Nama:'),
            'photo': ('Foto:'),
            'description': ('Deskripsi:'),
            'price': ('Harga:'),
            'discount': ('Diskon(%):'),
		}


