from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    matricula = models.CharField('Matricula ', max_length=50, blank=False)
    nome = models.CharField('Nome', max_length=100, blank=False)
    sexo = models.CharField('Sexo', max_length=1)
    cpf = models.CharField('Cpf ', max_length=11, blank=False)
    rg = models.CharField('Rg ', max_length=7)
    telefone = models.CharField('Telefone', max_length= 11)
    email = models.CharField('Email', max_length=50)
    dataNascimento = models.DateTimeField(default=timezone.now, blank=False)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='imagens/', null=False, blank=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #biometria

    def ___str___(self):
        return self.nome+" - "+self.cpf


class Curso(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

class Turno(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

class Turma(models.Model):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    turno = models.ForeignKey('Turno', on_delete=models.CASCADE)
    descricao = models.CharField('Descrição', max_length=100)

class Servidor(models.Model):
    nome= models.CharField('Nome', max_length=100, blank=False)
    sexo = models.CharField('Sexo', max_length=1)
    suap = models.CharField('Suap', max_length=30, blank=False)
    dataIngresso = models.DateTimeField(verbose_name='Data de Ingresso')
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    #credito = models.CharField('Crédito', max_length=30)

class Refeicao(models.Model):
    usuarioCadastro = models.ForeignKey('auth.User', related_name='usuario_cadastro', on_delete=models.CASCADE)
    data = models.DateTimeField(verbose_name="Data")
    quantidadeLimite = models.IntegerField('Quantidade Limite')
    descricao = models.CharField('Descricao', max_length=100)
    slide = models.CharField('Slide', max_length=100)
    refeicao = models.CharField('Refeicao', max_length=100)
    tipoRefeicao = models.ForeignKey('TipoRefeicao', on_delete=models.PROTECT)

class TipoRefeicao(models.Model):
    descricao = models.CharField('Descricao', max_length=100)
    horaInicio = models.DateTimeField()
    horaFim = models.DateTimeField()
    horaInicioReserva = models.DateTimeField()
    horaFimReserva= models.DateTimeField()

class Reserva(models.Model):
    refeicao = models.ForeignKey('Refeicao', on_delete=models.CASCADE)
    usuarioReserva = models.ForeignKey('auth.User', related_name='usuario_reserva', on_delete=models.CASCADE)
    usuarioPendencia = models.ForeignKey('auth.User', related_name='usuario_pendencia', on_delete=models.CASCADE)
    dataReserva = models.DateTimeField()
    dataConfirmacaoReserva = models.DateTimeField()
    dataRetiradaPendecia = models.DateTimeField()
