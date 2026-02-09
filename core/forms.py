from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Descripción...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0.00'}),
            'imagen': forms.FileInput(attrs={'class': 'form-file'}),
        }

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({'class': 'form-input'})
