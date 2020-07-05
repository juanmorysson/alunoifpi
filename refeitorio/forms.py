from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = ('foto','matricula','nome','sexo', 'cpf', 'rg','telefone','email', 'dataNascimento','usuario','ativo',)
        
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        
        
class CursoForm(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = ('descricao',)
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        
     
class TurnoForm(forms.ModelForm):
    
    class Meta:
        model = Turno
        fields = ('descricao',)
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        

class TurmaForm(forms.ModelForm):
    
    class Meta:
        model = Turma
        fields = ('descricao','curso','turno',)
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        

class ServidorForm(forms.ModelForm):
    
    class Meta:
        model = Servidor
        fields = ('nome','sexo', 'suap', 'dataIngresso','usuario',)
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        
             
class RefeicaoForm(forms.ModelForm):
    
    class Meta:
        model = Refeicao
        fields = ('data','quantidadeLimite','descricao','slide', 'refeicao', 'tipoRefeicao',)
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        

class TipoRefeicaoForm(forms.ModelForm):
    
    class Meta:
        model = TipoRefeicao
        fields = ('descricao','horaInicio','horaFim','horaInicioReserva', 'horaFimReserva',)
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ('refeicao',)
        
        widgets = {
        }
        
     