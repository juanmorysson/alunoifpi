from django import forms
from .models import Noticia

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ('photo','destaque','title', 'text', )
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={"rows":5, "cols":20,'class': 'form-control'}),
        }
        
        
        
        
        