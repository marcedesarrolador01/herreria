from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tu nombre',
        'id': 'nombre'
    }))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'tu@correo.com',
        'id': 'email'
    }))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Escribe tu mensaje aquí...',
        'rows': 4,
        'id': 'mensaje'
    }))
