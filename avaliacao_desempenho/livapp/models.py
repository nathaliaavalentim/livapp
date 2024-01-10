import datetime
from django.db import models
from django.utils import timezone
import cv2
from ecapture import ecapture as ec
from django.contrib.auth.models import User
from django.utils.timezone import now




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        
class Dados(models.Model):
    #id = CompositeKey(columns=['id', 'ciclo'])
    #id = models.ForeignKey(auth_user, models.DO_NOTHING,db_column='id')    
    #aluno = models.CharField(max_length=200, default='Aluno')
    #aluno = models.ManyToOneField(User, on_delete=models.CASCADE)
    TEMAS_CHOICES = (
        ('Bola', 'Bola'),
        ('Carro', 'Carro'),
        ('Doce', 'Doce'),
        ('Livro', 'Livro'),
    )
    AVATAR_CHOICES = (
        ('Menina2', 'Menina2'),
        ('Cachorro', 'Cachorro'),
        ('Menina', 'Menina'),
        ('Menino', 'Menino'),
        ('Coelho', 'Coelho'),
        ('Emoji', 'Emoji'),
    )
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    ciclo = models.AutoField(primary_key=True)
    avatar = models.CharField(max_length=200, choices=AVATAR_CHOICES)
    tema_1 = models.CharField(max_length=200, choices=TEMAS_CHOICES)
    tema_2 = models.CharField(max_length=200, choices=TEMAS_CHOICES)
    tema_3 = models.CharField(max_length=200, choices=TEMAS_CHOICES)
    tema_4 = models.CharField(max_length=200, choices=TEMAS_CHOICES)
    def __str__(self):
        return str(self.aluno)
    
    class Meta:
        managed = True
        db_table = 'dados'
        unique_together = (('aluno', 'ciclo'),)


class Performance(models.Model):    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    acerto = models.CharField(max_length=200,null=True)
    uuid = models.CharField(max_length=200,null=True)
    exercicio = models.CharField(max_length=200,null=True)
    performance = models.FloatField(default=0,null=True)
    tempo = models.FloatField(default=0,null=True)
    pontuacao_anterior = models.FloatField(default=0,null=True)
    pontuacao_atual = models.FloatField(default=0,null=True)
    date = models.DateTimeField(default=now, editable=False)
    distancia = models.FloatField(default=0,null=True)

    def __str__(self):
        return str(self.aluno)
   
    class Meta:
        managed = True
        db_table = 'performance'

class Contador(models.Model):    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    exercicio = models.CharField(max_length=200)
    tentativa = models.IntegerField(blank=True, null=True)
    tempo = models.CharField(max_length=200)
    acerto = models.CharField(max_length=200)
    erro = models.CharField(max_length=200) 
    latencia = models.CharField(max_length=200, default='0')
    coordenadaX = models.CharField(max_length=200, default='0')
    coordenadaY = models.CharField(max_length=200, default='0')
    latencia2 = models.CharField(max_length=200, default='0')
    coordenadaX2 = models.CharField(max_length=200, default='0')
    coordenadaY2 = models.CharField(max_length=200, default='0')
    latencia3 = models.CharField(max_length=200, default='0')
    coordenadaX3 = models.CharField(max_length=200, default='0')
    coordenadaY3 = models.CharField(max_length=200, default='0')
    latencia4 = models.CharField(max_length=200, default='0')
    coordenadaX4 = models.CharField(max_length=200, default='0')
    coordenadaY4 = models.CharField(max_length=200, default='0')
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return str(self.aluno)
   
    class Meta:
        managed = True
        db_table = 'contador'
        
        
class Parametro(models.Model):    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    tempoIdeal = models.IntegerField(default=5)
    tempoSatisfatorio = models.IntegerField(default=15)
    reforcoForte = models.FloatField(default=1.3)
    reforcoMedio = models.FloatField(default=1.2)
    reforcoFraco = models.FloatField(default=1.1)
    pontuacaoMaxima = models.IntegerField(default=10)
    pontuacaoMedia = models.IntegerField(default=5)
    pontuacaoMinima = models.IntegerField(default=1)
    pontuacaoFinal = models.IntegerField(default=100)
    date = models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return str(self.aluno)
   
    class Meta:
        managed = True
        db_table = 'parametro'



class Usuarios(models.Model):    
    user = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    key = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.user)
   
    class Meta:
        managed = True
        db_table = 'usuarios'


class DesempenhoSessao(models.Model):    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacaoSessao = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.aluno)
   
    class Meta:
        managed = True
        db_table = 'desempenho'

