from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    """Formulário de Login com estilização de luxo"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'luxury-input',
        'placeholder': 'Usuário'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'luxury-input',
        'placeholder': 'Senha'
    }))

class RegistroForm(UserCreationForm):
    """Formulário de Cadastro baseado no User model do Django"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'luxury-input',
        'placeholder': 'E-mail'
    }))

    class Meta:
        model = User
        fields = ("username", "email")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica a classe de estilo a todos os campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'luxury-input'})