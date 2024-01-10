from django.forms import ModelForm
from .models import Dados #<br>
class PostForm(ModelForm):
    class Meta:
        model = Dados
        fields = ['ciclo', 'avatar', 'tema_1', 'tema_2', 'tema_3', 'tema_4']
        
        
        
        
