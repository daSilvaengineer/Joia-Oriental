from django import forms
import re

class CheckoutForm(forms.Form):
    first_name = forms.CharField(
        label="Nome",
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu nome',
            'autocomplete': 'given-name',
            'class': 'form-control',
        })
    )

    last_name = forms.CharField(
        label="Sobrenome",
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu sobrenome',
            'autocomplete': 'family-name',
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            'placeholder': 'seu@email.com',
            'autocomplete': 'email',
            'class': 'form-control',
        })
    )

    address = forms.CharField(
        label="Endereço",
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Rua, número, complemento',
            'autocomplete': 'street-address',
            'class': 'form-control',
        })
    )

    city = forms.CharField(
        label="Cidade",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Cidade',
            'autocomplete': 'address-level2',
            'class': 'form-control',
        })
    )

    zip_code = forms.CharField(
        label="CEP",
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '00000-000',
            'autocomplete': 'postal-code',
            'class': 'form-control',
        })
    )

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')
        zip_code = re.sub(r'\D', '', zip_code)
        if len(zip_code) != 8:
            raise forms.ValidationError("O CEP deve conter 8 dígitos.")
        return f"{zip_code[:5]}-{zip_code[5:]}"