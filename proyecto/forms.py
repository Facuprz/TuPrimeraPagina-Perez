# proyecto/forms.py
from django import forms
from .models import Page
from ckeditor.widgets import CKEditorWidget

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
        widgets = {
            'contenido': CKEditorWidget(),
        }

class PageSearchForm(forms.Form):
    q = forms.CharField(
        label='Buscar',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar páginas...'})
    )
