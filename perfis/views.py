from django.shortcuts import render
from perfis.models import Perfil
# Create your views here.

def index(request):
    return render(request,'index.html',{'perfis':Perfil.objects.all()})   

def exibir(request,perfil_id):
    print ('Id do perfil do usuário : %s' %(perfil_id))

    #instancia de um novo objeto
    #perfil = Perfil()
    perfil = Perfil.objects.get(id=perfil_id)
    
    #variavel perfil_id recebida como parametro no metodo exibir.
    #if perfil_id == '1':
    #    perfil = Perfil('Gilmar de Jesus Santana','gil@gil.com.br','88888888888','Gilunix')
        
    #if perfil_id == '2':
    #    perfil = Perfil('Renata','renata@gil.com.br','9999998','Gilunix')
    return render(request,'perfil.html',{"perfil":perfil})
