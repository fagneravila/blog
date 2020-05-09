# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    
    def Clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('email_comentario')
        
        
        if len(nome) < 5:
            self.add_error(
                'nome_comentario'
                'Nome precisa de termaide 5 caracteres'
                )
            
        if not comentario:
            self.add_error(
                'comentario'
                'vc nao comentou'
                )
    
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
   



