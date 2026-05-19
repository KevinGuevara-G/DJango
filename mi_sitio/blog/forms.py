from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Especificamos qué campos del modelo queremos mostrar en el formulario
        fields = ['titulo', 'contenido']