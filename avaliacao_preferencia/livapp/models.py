import datetime
from django.db import models
from django.utils import timezone
import cv2
from ecapture import ecapture as ec
from django.contrib.auth.models import User





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
        #('Super Heroi', 'Super Heroi'),
        #('Cachorro', 'Cachorro'),
        #('McQueen', 'McQueen'),
        #('Trem', 'Trem'),
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



    








