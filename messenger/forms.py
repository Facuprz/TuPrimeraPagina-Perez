# messenger/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    """Formulario para redactar/enviar un mensaje."""
    recipient = forms.ModelChoiceField(queryset=User.objects.none(), label="Para")

    class Meta:
        model = Message
        fields = ['recipient', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje...'}),
        }

    def __init__(self, *args, **kwargs):
        # Permitimos pasar el usuario actual para excluirlo del selector
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        qs = User.objects.all()
        if user is not None:
            qs = qs.exclude(id=user.id)
        self.fields['recipient'].queryset = qs
        self.fields['recipient'].label_from_instance = lambda u: f"{u.username} ({u.email or 'sin email'})"


class ReplyForm(forms.ModelForm):
    """Formulario sencillo para responder en un hilo."""
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Responder...'}),
        }
