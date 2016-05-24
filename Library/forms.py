from django import forms
from .models import Vinyl, User


class AddVinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ['artist', 'title', 'year', 'genre', 'label', 'format_size', 'isbn']
        widgets = {
            'artist': forms.TextInput(
                attrs={'id': 'artist', 'class': 'form-control'}
            ),
            'title': forms.TextInput(
                attrs={'id': 'title', 'class': 'form-control'}
            ),
            'year': forms.TextInput(
                attrs={'id': 'year', 'class': 'form-control'}
            ),
            'label': forms.TextInput(
                attrs={'id': 'label', 'class': 'form-control'}
            ),
            'label': forms.TextInput(
                attrs={'id': 'label', 'class': 'form-control'}
            ),
            'format_size': forms.TextInput(
                attrs={'id': 'format_size', 'class': 'form-control'}
            ),
            'isbn': forms.TextInput(
                attrs={'id': 'isbn', 'class': 'form-control'}
            ),
        }

class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={'id': 'username', 'class': 'form-control'}
            ),
            'first_name': forms.TextInput(
                attrs={'id': 'first_name', 'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'id': 'last_name', 'class': 'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'id': 'email', 'class': 'form-control'}
            ),
        }