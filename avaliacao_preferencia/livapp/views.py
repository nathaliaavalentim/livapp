
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
import cv2
from ecapture import ecapture as ec
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path, os
from django.views.decorators.cache import never_cache
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import time
import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Dados
from .forms import PostForm

def home(request):
    return render(request, 'exe1.html', {'what':'Django File Upload'})
    
def home2(request):
    return render(request, 'reforco.html', {'what':'Django File Upload'})
    
def home3(request):
    return render(request, 'dica.html', {'what':'Django File Upload'})
    
def home4(request):
    return render(request, 'exe2.html', {'what':'Django File Upload'})
    
def home5(request):
    return render(request, 'exe1rep.html', {'what':'Django File Upload'})
    
def home6(request):
    return render(request, 'reforco2.html', {'what':'Django File Upload'})
    
def home7(request):
    return render(request, 'dica2.html', {'what':'Django File Upload'})   

def home8(request):
    return render(request, 'exe2rep.html', {'what':'Django File Upload'})
    
def home9(request):
    return render(request, 'exe3.html', {'what':'Django File Upload'})
    
def home10(request):
    return render(request, 'reforco3.html', {'what':'Django File Upload'})
    
def home11(request):
    return render(request, 'dica3.html', {'what':'Django File Upload'})   

def home12(request):
    return render(request, 'exe1rep.html', {'what':'Django File Upload'})
    
def home13(request):
    return render(request, 'exe3ant.html', {'what':'Django File Upload'})

def salvaavatar(request):
    print(request.GET['nome'])
    request.session['avatar'] = request.GET['nome']
    request.session.modified = True
    request.session.save()
    return HttpResponse(request.session['avatar'])
    
def recuperaavatar(request):
    print(request.session['avatar'])
    return HttpResponse(request.session['avatar'])
  



  





#criar apenas uma fun��o de upload
def upload(request):
    if request.method == 'POST':
    
       
        file_name = ''
        redireciona = ''
        tema = request.POST['tema']
        user = request.user
        
        if request.POST['pagina'] == 'exe1':
            file_name = "exercicio1.jpeg"
            redireciona = "livapp/pictureexrep1"
            
        if request.POST['pagina'] == 'exe2':
            file_name = "exercicio2.jpeg"
            redireciona = "livapp/pictureexrep2"
            
        if request.POST['pagina'] == 'exe3':
            file_name = "exercicio3.jpeg"
            redireciona = "livapp/pictureexrep3"
            
        
 ###########################################################       
        

        if request.POST['pagina'] == 'reforco':
            file_name = "reforco.jpeg"             
            redireciona = "livapp/pictureex2"
            
        if request.POST['pagina'] == 'dica':
            file_name = "dica.png"      
            redireciona = "livapp/pictureexrep1"
            
        if request.POST['pagina'] == 'reforco2':
            file_name = "reforco2.png"                       
            redireciona = "livapp/pictureex3"
            
        if request.POST['pagina'] == 'dica2':
            file_name = "dica2.png"            
            redireciona = "livapp/pictureexrep2"
            
        if request.POST['pagina'] == 'reforco3':
            file_name = "reforco3.png"            
            redireciona = "livapp/picturereforco3"
            time.sleep(3)
            redireciona = "livapp/final"
 
        if request.POST['pagina'] == 'dica3':
            file_name = "dica3.png"            
            redireciona = "livapp/pictureexrep3"
        
        #if request.POST['pagina'] == 'final':
        #    redireciona = "livapp/final"
        
        file_name = str(user)+'_'+tema+'_'+file_name
        
        base64_data = request.POST['file'][22:]
        #print(base64_data)
        decode_image = base64.b64decode(base64_data)
        data = ContentFile(decode_image)  
        handle_uploaded_file(data, file_name)
        #time.sleep(2)   
        #t = loader.get_template(redireciona)
        c = {'foo': 'bar'}
        #return HttpResponse(t.render(c, request)) 
        
        return HttpResponse("sucesso")
            
        
    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
             destination.write(chunk)


############################################################################

class IndexView(generic.ListView):
    template_name = 'livapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'livapp/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'livapp/results.html'





def avatar(request): 
    t = loader.get_template('livapp/avatar.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picture(request): 
    t = loader.get_template('livapp/temas.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))
    #return redirect('temas.html')

#Exercício 1
def pictureex(request):
    t = loader.get_template('livapp/exe1.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))   
    
def pictureexrep1(request):
    t = loader.get_template('livapp/exe1rep.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturereforco(request):
    t = loader.get_template('livapp/reforco.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedica(request):
    t = loader.get_template('livapp/dica.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
    
#Exercício 2
def pictureex2(request):
    t = loader.get_template('livapp/exe2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureexrep2(request):
    t = loader.get_template('livapp/exe2rep.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturereforco2(request):
    t = loader.get_template('livapp/reforco2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturedica2(request):
    t = loader.get_template('livapp/dica2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    

#Exercício 3    
def pictureex3(request):
    t = loader.get_template('livapp/exe3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureexant3(request):
    t = loader.get_template('livapp/exe3ant.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturereforco3(request):
    t = loader.get_template('livapp/reforco3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturedica3(request):
    t = loader.get_template('livapp/dica3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def final(request):
    t = loader.get_template('livapp/final.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
    
    
    
################################################################################    
    
    
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

#def index(request):
#    return HttpResponse("Seja bem-vindo!")
    
def detail(request, question_id):
    return HttpResponse("Você está olhando para uma questão %s." % question_id)

def results(request, question_id):
    response = "Você está olhando para os resultados da questão %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você esta votando %s." % question_id)      
    
    
    
    
    
#############################################################################################
#def avatar(request):
#    t = loader.get_template('livapp/avatar.html')
#    c = {'foo': 'bar'}
#    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')
   
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'livapp/index.html', context)
    
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('livapp/index.html')
#    }
#    context = {
#        'latest_question_list': latest_question_list,
#    return HttpResponse(template.render(context, request))
    
    
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'livapp/detail.html', {'question': question})
    
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'livapp/results.html', {'question': question})

def vote1(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'livapp/detail.html', {
            'question': question,
            'error_message': "Você não selecionou.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('livapp:results', args=(question.id,)))
        
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/livapp/logar_usuario')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'livapp/cadastro.html', {'form_usuario': form_usuario})
    
    
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/livapp/avatar')            
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'livapp/index.html', {'form_login': form_login})
    #return redirect('/livapp', {'form_login': form_login})

def index(request):  
    t = loader.get_template('livapp/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))
    
################################################################################################


@login_required
def post_create(request):
    form = PostForm()
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            #post_aluno = form.cleaned_data['aluno']
            #post_ciclo = form.cleaned_data['ciclo']
            post_avatar = form.cleaned_data['avatar']
            post_tema_1 = form.cleaned_data['tema_1']
            post_tema_2 = form.cleaned_data['tema_2']
            post_tema_3 = form.cleaned_data['tema_3']
            post_tema_4 = form.cleaned_data['tema_4']
            new_post = Dados( avatar=post_avatar, tema_1=post_tema_1, tema_2=post_tema_2, tema_3=post_tema_3,tema_4=post_tema_4)
            new_post = form.save(commit=False)
            new_post.aluno = request.user                  
            new_post.save()
            return redirect('livapp:avatar')
    elif(request.method == 'GET'):
        return render(request, 'livapp/avatar.html', {'form': form})
        
# def post_create(request):
#     form = PostForm()
#     if(request.method == 'POST'):
#         form = PostForm(request.POST)
#         if(form.is_valid()):
#             #post_aluno = form.cleaned_data['aluno']
#             #post_ciclo = form.cleaned_data['ciclo']
#             post_avatar = form.cleaned_data['avatar']
#             post_tema_1 = form.cleaned_data['tema_1']
#             post_tema_2 = form.cleaned_data['tema_2']
#             post_tema_3 = form.cleaned_data['tema_3']
#             post_tema_4 = form.cleaned_data['tema_4']
#             new_post = Dados( avatar=post_avatar, tema_1=post_tema_1, tema_2=post_tema_2, tema_3=post_tema_3,tema_4=post_tema_4)
#             new_post = form.save(commit=False)
#             new_post.aluno = request.user                  
#             new_post.save()
#             return redirect('livapp:avatar')
#     elif(request.method == 'GET'):
#         return render(request, 'livapp/avatar.html', {'form': form})
        
def salvaavatarbd(request):
  
    if(request.method == 'GET'):        
        post_avatar = request.GET.get('avatar')
        post_tema_1 = request.GET.get('tema_1')
        post_tema_2 = request.GET.get('tema_2')
        post_tema_3 = request.GET.get('tema_3')
        post_tema_4 = request.GET.get('tema_4')
        new_post = Dados( avatar=post_avatar, tema_1=post_tema_1, tema_2=post_tema_2, tema_3=post_tema_3,tema_4=post_tema_4)
        #new_post = form.save(commit=False)
        new_post.aluno = request.user                  
        new_post.save()
    return redirect('livapp:avatar')
   
   





















    

