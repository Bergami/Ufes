# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.
class Projeto(models.Model):
    nome  = models.CharField(max_length = 100)
    objetivo = models.TextField()
    palavras_chaves= models.TextField()
    data_cadastro = models.DateField(default=datetime.now, editable=False)
    
    class Meta:
        db_table = 'Projeto'    
    
    def __unicode__(self):
        return self.nome
        #return  "Nome: %s , Objetivo: %s, Chaves: %s" %(self.nome , self.objetivo, self.palavras_chaves)
    
class Grupo(models.Model):
    nome  = models.CharField(max_length = 100)    
    projeto_id = models.ForeignKey(Projeto)
    
    class Meta:
        db_table = 'Grupo'
        
    def __unicode__(self):
        return self.nome
        #return "Nome: %s , Projeto: $d" % (self.nome, self.projeto_id)

class Usuario(models.Model):
    nome  = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    senha = models.CharField(max_length = 20)
    grupo = models.ForeignKey(Grupo)
    
    
    class Meta:
        db_table = 'Usuario'
        
    def __unicode__(self):
        return self.nome
        #return  "Nome: %s, Email: %s, Grupo: %d" % (self.nome , self.email, self.grupo)


class Documento(models.Model):
    titulo = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    data_publicacao = models.CharField(max_length = 10)
    tag = models.CharField(max_length = 250)    
    arquivo = models.BinaryField()
    resumo_em_html = models.TextField()
    classificacao = models.IntegerField(default=0) 
    
    
    
    class Meta:
        db_table = 'Documento'

    def __unicode__(self):
        return self.Titulo
        #return  "Nome: %s, Email: %s, Grupo: %d" % (self.nome , self.email, self.grupo)
