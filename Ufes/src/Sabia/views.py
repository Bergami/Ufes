# coding: utf-8
# Create your views here.
from django.forms import ModelForm
from Sabia.models import *
from django.http import HttpResponse
from django.core.context_processors import csrf

from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.db.models.sql.datastructures import Date


# pagina inicial do projeto django-wars
def index(request):
    return render_to_response("index.html", RequestContext(request, {}))    
    #return render_to_response("index.html")

class DocumentosModelForm(ModelForm):
    class Meta:
        model = Documento


def autenticar_usuario(request):
    u = {}
    u.update(csrf(request))
    if request.POST:                        
        email = request.POST['email']        
        senha = request.POST['senha']        

        usu = Usuario.objects.filter(email__exact=email)
        usu = usu.filter(senha__exact=senha)

        if usu is not None:
            request.session['usuario_ativo'] = usu


def usuario(request): 
    grupo = Grupo.objects.all()
    return render_to_response("CadastroUsuario.html", {'grupo': grupo}, context_instance=RequestContext(request))
        

def salvar_usuario(request):
    u = {}
    u.update(csrf(request))
    if request.POST:        
        usu = Usuario()        
        usu.nome = request.POST['nome']
        usu.email = request.POST['email']
        usu.senha = request.POST['senha']
        usu.grupo_id = request.POST['grupo_id']
        usu.save()

        return render_to_response('CadastroUsuario.html')
        


def documento(request): 
    return render_to_response("CadastroDocumento.html", RequestContext(request, {}))  
    #return render_to_response("CadastroDocumento.html")


def salvar_documento(request):
    d = {}
    d.update(csrf(request))
    if request.POST:        
        doc = Documento()
        doc.titulo = request.POST['titulo']
        doc.autor = request.POST['autor']
        doc.data_publicacao = request.POST['data_publicacao']
        doc.resumo_em_html =  request.POST['resumo_em_html']  
        doc.tag = request.POST['tag']      
        doc.classificacao = request.POST["classificacao"]        
        
        doc = doc.save()
        #form = DocumentosModelForm(request)        
        return render_to_response('CadastroDocumento.html')
        