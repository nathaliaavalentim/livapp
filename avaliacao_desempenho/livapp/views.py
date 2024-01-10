
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
from django.http import JsonResponse
from .models import Dados
from .models import Contador
from .models import Parametro
from .models import Performance
from .models import Usuarios
from .forms import PostForm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import bleedfacedetector as fd
import time
import math
import json
import sys
from pathlib import Path

def homer(request):
    return render(request, 'reforco.html', {'what':'Django File Upload'})
    
def homed(request):
    return render(request, 'dica.html', {'what':'Django File Upload'})


def home(request):
    return render(request, 'exe1.html', {'what':'Django File Upload'})
    
def home12(request):
    return render(request, 'exe1n2.html', {'what':'Django File Upload'})
    
def home13(request):
    return render(request, 'exe1n3.html', {'what':'Django File Upload'}) 

def home14(request):
    return render(request, 'exe1n4.html', {'what':'Django File Upload'}) 
    

    
def home21(request):
    return render(request, 'exe2.html', {'what':'Django File Upload'})
   
def home22(request):
    return render(request, 'exe2n2.html', {'what':'Django File Upload'}) 
    
def home23(request):
    return render(request, 'exe2n3.html', {'what':'Django File Upload'})    
    
def home24(request):
    return render(request, 'exe2n4.html', {'what':'Django File Upload'}) 



def home31(request):
    return render(request, 'exe3.html', {'what':'Django File Upload'})

def home32(request):
    return render(request, 'exe3n2.html', {'what':'Django File Upload'})   
    
def home33(request):
    return render(request, 'exe3n3.html', {'what':'Django File Upload'})  

def home34(request):
    return render(request, 'exe3n4.html', {'what':'Django File Upload'})     
    
    

def home41(request):
    return render(request, 'exe4.html', {'what':'Django File Upload'})    
    
def home42(request):
    return render(request, 'exe4n2.html', {'what':'Django File Upload'})  

def home43(request):
    return render(request, 'exe4n3.html', {'what':'Django File Upload'}) 
    
def home44(request):
    return render(request, 'exe4n4.html', {'what':'Django File Upload'})     
    
    

def home51(request):
    return render(request, 'exe5.html', {'what':'Django File Upload'})       

def home52(request):
    return render(request, 'exe5n2.html', {'what':'Django File Upload'})       

def home53(request):
    return render(request, 'exe5n3.html', {'what':'Django File Upload'})  

def home54(request):
    return render(request, 'exe5n4.html', {'what':'Django File Upload'})    



def home61(request):
    return render(request, 'exe6.html', {'what':'Django File Upload'})    
    
def home62(request):
    return render(request, 'exe6n2.html', {'what':'Django File Upload'})    

def home63(request):
    return render(request, 'exe6n3.html', {'what':'Django File Upload'})  

def home64(request):
    return render(request, 'exe6n4.html', {'what':'Django File Upload'})     



def salvaavatar(request):
    print(request.GET['nome'])
    request.session['avatar'] = request.GET['nome']
    request.session.modified = True
    request.session.save()
    return HttpResponse(request.session['avatar'])
    
def recuperaavatar(request):
    print(request.session['avatar'])
    return HttpResponse(request.session['avatar'])
  

def qlearning(request):

    parametro = Parametro.objects.filter(aluno_id = request.user).order_by('-date').first()
    
    tempoIdeal = int(getattr(parametro,'tempoIdeal'))
    tempoSatisfatorio = int(getattr(parametro,'tempoSatisfatorio'))
    reforcoForte = float(getattr(parametro,'reforcoForte'))
    reforcoMedio = float(getattr(parametro,'reforcoMedio'))
    reforcoFraco = float(getattr(parametro,'reforcoFraco'))
    pontuacaoMaxima = int(getattr(parametro,'pontuacaoMaxima'))
    pontuacaoMedia = int(getattr(parametro,'pontuacaoMedia'))
    pontuacaoMinima = int(getattr(parametro,'pontuacaoMinima'))
    pontuacaoFinal = int(getattr(parametro,'pontuacaoFinal'))
    
    #performance = float(getattr(parametro,'performance'))
    #satisfacao = float(getattr(parametro,'satisfacao'))
    #distanciaEuclidiana = float(getattr(parametro,'distanciaEuclidiana'))
   
 
    
    if request.method == 'GET':
        hash = {"0":"pictureex",
                "4":"pictureex2",
                "8":"pictureex3",
                "12":"pictureex4",
                "16":"pictureex5",
                "20":"pictureex6",
                "24":"pictureex1n2",
                "28":"pictureex2n2",
                "32":"pictureex3n2",
                "36":"pictureex4n2",
                "40":"pictureex5n2",
                "44":"pictureex6n2",
                "48":"pictureex1n3",
                "52":"pictureex2n3",
                "56":"pictureex3n3",
                "60":"pictureex4n3",
                "64":"pictureex5n3",
                "68":"pictureex6n3",
                "72":"pictureex1n4",
                "76":"pictureex2n4",
                "80":"pictureex3n4",
                "84":"pictureex4n4",
                "88":"pictureex5n4",
                "92":"pictureex6n4"}
                
        tempo = int(request.GET.get('tempo'))
        acerto = request.GET.get('acerto')
        pontuacao = int(request.GET.get('pontuacao'))
        imagem = request.GET.get('imagem')
        
        print(acerto)
        
        if pontuacao is None or pontuacao < 0:
            pontuacao = 0
                 
        # %%
        # Set model path
        #print(Path(__file__).parent)
        my_local_file = os.path.join(Path(__file__).parent, 'cnn/EmotionRecognition/Model/emotion-ferplus-8.onnx')
        print(my_local_file)
        model = os.path.join(Path(__file__).parent, 'cnn/EmotionRecognition/Model/emotion-ferplus-8.onnx')
        net = cv2.dnn.readNetFromONNX(model)
        
        # %%
        """
        ##  <font style="color:rgb(134,19,348)">Read Image</font> 
        
        """
        print(imagem)
        
        distancia = float(request.GET.get('distancia'))
        
        print('\n\n\n\nDISTANCIA')
        print(distancia)
        
        performance = 0.0
        
        
        
        if(imagem):
            print(str(imagem))
            # %%
            # Read image
            my_local_file = os.path.join(Path(__file__).parent.parent, "upload/"+str(imagem))
            print(my_local_file)
            image = cv2.imread(os.path.join(Path(__file__).parent.parent, "upload/"+str(imagem)))
            
            # Display image
            try:
                plt.figure(figsize=[10,10])
                #plt.imshow(image[:,:,::-1])
                plt.axis('off');
                
                # %%
                """
                **We'll be predicting among these Emotions.**
                """
                
                # %%
                # Define the emotions
                emotions = ['Neutral', 'Happy', 'Surprise', 'Sad', 'Anger', 'Disgust', 'Fear', 'Contempt']
                
                # %%
                """
                ##  <font style="color:rgb(134,19,348)">Detect faces with bleedfacedetector</font> 
                """
                
                # %%
                img_copy = image.copy()
                
                # Use SSD detector with 20% confidence threshold.
                faces = fd.ssd_detect(img_copy, conf=0.2)
                
                # Check the number detected faces in image
                print("{} faces detected".format(len(faces)))
                
                # Lets take coordinates of the first face in the image. 
                x,y,w,h = faces[0]
                
                # Define padding for face roi
                padding = 3
                
                # extract the Face from image with padding.
                padded_face = img_copy[y-padding:y+h+padding,x-padding:x+w+padding] 
                
                # %%
                """
                ##  <font style="color:rgb(134,19,348)">Padded vs Non Padded face  </font>
                """
                
                # %%
                # Non Padded face
                face = img_copy[y:y+h, x:x+w] 
                
                # Just increasing the padding for demo purpose
                padding = 20
                
                # Get the Padded face
                padded_face_demo = img_copy[y-padding:y+h+padding,x-padding:x+w+padding] 
                
                plt.figure(figsize=[10, 10])
                plt.subplot(121);plt.imshow(padded_face_demo[...,::-1]);plt.title("Padded face");plt.axis('off')
                plt.subplot(122);plt.imshow(face[...,::-1]);plt.title("Non Padded face");plt.axis('off');
                
                # %%
                """
                ##  <font style="color:rgb(134,19,348)"> Pre-processing the image  </font>
                """
                
                # %%
                gray = cv2.cvtColor(padded_face,cv2.COLOR_BGR2GRAY)
                resized_face = cv2.resize(gray, (64, 64))
                processed_face = resized_face.reshape(1,1,64,64)
                
                # %%
                """
                ## <font style="color:rgb(134,19,348)"> Input the Blob Image to the Network  </font>
                
                """
                
                # %%
                net.setInput(processed_face)
                
                # %%
                """
                ##  <font style="color:rgb(134,19,348)">Forward Pass</font> 
                
                """
                
                # %%
                #%%time
                Output = net.forward()
                
                # %%
                
                
                # %%
                """
                ###  <font style="color:rgb(134,19,348)">Apply Softmax function to get Class Probabilities</font> 
                Now that we have scores for each class, we will convert these scores to probabilities between 0-1 by using a softmax function.
                """
                
                # %%
                # Compute softmax values for each sets of scores  
                expanded = np.exp(Output - np.max(Output))
                probablities =  expanded / expanded.sum()
                
                # Get the final probablities 
                prob = np.squeeze(probablities)
                
                
                
                # %%
                # Get the index of the max probability and that's your predicted emotion
                predicted_emotion = emotions[prob.argmax()]
                
                # Print the target Emotion
                print('Predicted Emotion is :{}'.format(predicted_emotion ))
                
                satisfacao = 0
                
                if predicted_emotion == "Happy" or predicted_emotion == "Surprise":
                    satisfacao = 1                  
                elif predicted_emotion == "Neutral":
                    satisfacao = 0.5
                else:
                    satisfacao = 0.1
                
                if acerto == "true":
                    performance = ((satisfacao * (100))/ tempo)                   
                else:
                    performance = ((satisfacao * (100/distancia))/ tempo)
                    
                  
            except:
                print("Problema ao classificar")
                
                
        if(pontuacao < 0):
            pontuacao = 0;
                   
        post_exercicio = request.GET.get('exercicio')        
        now = timezone.now()
        new_post = Performance(exercicio=post_exercicio, date = now)
        #new_post = form.save(commit=False)
        new_post.aluno = request.user  
        new_post.uuid = request.GET.get('uuid')
        
        new_post.pontuacao_anterior = int(request.GET.get('pontuacao'))
        
        value_tmp = request.GET.get('distancia')
        
        if value_tmp is None:
            value_tmp = 0
            
        
        new_post.distancia = (0 if acerto == "true" else float(value_tmp))
       
        
        new_post.acerto = request.GET.get('acerto')
        new_post.tempo = int(request.GET.get('tempo'))
        
        if performance is None or performance <= 0.0:
            if acerto == "true":
                performance = ((0.5 * (100))/ tempo)                   
            else:
                performance = ((0.5 * (100/distancia))/ tempo)
        
        
        
        print('AQUIIIIII')
        print(pontuacao)
        print(performance)
        pontuacao += performance
   
        pagina = 'final'
        
        points = pontuacao
        
        new_post.performance = performance
        new_post.pontuacao_atual = pontuacao
        
        new_post.save()
        
        
        
        if(pontuacao < pontuacaoFinal):
            if(points > 0):
                points = math.floor(points)
                mod = points % 4;
                points = points - mod;
                
                
            pagina = hash[str(points)]
        
        print('AQUIIIIII2')
        retorno = {"pagina":pagina,
                   "pontuacao":math.floor(pontuacao)}
        
        
    
        print(retorno)
        return JsonResponse(retorno)
    

  





#criar apenas uma fun��o de upload
def upload(request):
    if request.method == 'POST':
    
       
        file_name = ''
        redireciona = ''
        tema = request.POST['tema']
        user = request.user
        
        if request.POST['pagina'] == 'reforco':
            file_name = "reforco.jpeg"             
            
            
        if request.POST['pagina'] == 'dica':
            file_name = "dica.png"  

#Upload N�vel 1
        
        
        if request.POST['pagina'] == 'exe1':
            file_name = "exercicio1N1.jpeg"
            
            
        if request.POST['pagina'] == 'exe2':
            file_name = "exercicio2N1.jpeg"
            
            
        if request.POST['pagina'] == 'exe3':
            file_name = "exercicio3N1.jpeg"
            
            
        if request.POST['pagina'] == 'exe4':
            file_name = "exercicio4N1.jpeg"
            
            
        if request.POST['pagina'] == 'exe5':
            file_name = "exercicio5N1.jpeg"            
            
            
        if request.POST['pagina'] == 'exe6':
            file_name = "exercicio6N1.jpeg"                 

#Upload N�vel 2

        if request.POST['pagina'] == 'exe1n2':
            file_name = "exercicio1N2.jpeg"
            
            
        if request.POST['pagina'] == 'exe2n2':
            file_name = "exercicio2N2.jpeg"
            
            
        if request.POST['pagina'] == 'exe3n2':
            file_name = "exercicio3N2.jpeg"
            
            
        if request.POST['pagina'] == 'exe4n2':
            file_name = "exercicio4N2.jpeg"
            
            
        if request.POST['pagina'] == 'exe5n2':
            file_name = "exercicio5N2.jpeg"            
            
            
        if request.POST['pagina'] == 'exe6n2':
            file_name = "exercicio6N2.jpeg"                
            

#Upload N�vel 3

        if request.POST['pagina'] == 'exe1n3':
            file_name = "exercicio1N3.jpeg"
            
            
        if request.POST['pagina'] == 'exe2n3':
            file_name = "exercicio2N3.jpeg"
            
            
        if request.POST['pagina'] == 'exe3n3':
            file_name = "exercicio3N3.jpeg"
            
            
        if request.POST['pagina'] == 'exe4n3':
            file_name = "exercicio4N3.jpeg"
            
            
        if request.POST['pagina'] == 'exe5n3':
            file_name = "exercicio5N3.jpeg"            
            
            
        if request.POST['pagina'] == 'exe6n3':
            file_name = "exercicio6N3.jpeg"   


#Upload N�vel 4

        if request.POST['pagina'] == 'exe1n4':
            file_name = "exercicio1N4.jpeg"
            
            
        if request.POST['pagina'] == 'exe2n4':
            file_name = "exercicio2N4.jpeg"
            
            
        if request.POST['pagina'] == 'exe3n4':
            file_name = "exercicio3N4.jpeg"
            
            
        if request.POST['pagina'] == 'exe4n4':
            file_name = "exercicio4N4.jpeg"
            
            
        if request.POST['pagina'] == 'exe5n4':
            file_name = "exercicio5N4.jpeg"            
            
            
        if request.POST['pagina'] == 'exe6n4':
            file_name = "exercicio6N4.jpeg"   
            
        
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
        
        return HttpResponse(file_name)
            
        
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



def parametro(request): 
    t = loader.get_template('livapp/parametrizacao.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  

def avatar(request): 
    t = loader.get_template('livapp/avatar.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picture(request): 
    t = loader.get_template('livapp/temas.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))
    #return redirect('temas.html')

#Exercicio 1
def pictureex(request):
    t = loader.get_template('livapp/exe1.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))   
    
def pictureex1n2(request):
    t = loader.get_template('livapp/exe1n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def pictureex1n3(request):
    t = loader.get_template('livapp/exe1n3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  

def pictureex1n4(request):
    t = loader.get_template('livapp/exe1n4.html')
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
    
def picturereforcoex1n2(request):
    t = loader.get_template('livapp/reforcoex1n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedicaex1n2(request):
    t = loader.get_template('livapp/dicaex1n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
    
    
    
    
#Exercicio 2
def pictureex2(request):
    t = loader.get_template('livapp/exe2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex2n2(request):
    t = loader.get_template('livapp/exe2n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex2n3(request):
    t = loader.get_template('livapp/exe2n3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex2n4(request):
    t = loader.get_template('livapp/exe2n4.html')
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
    
def picturereforcoex2n2(request):
    t = loader.get_template('livapp/reforcoex2n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedicaex2n2(request):
    t = loader.get_template('livapp/dicaex2n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
    
    
    
    
    

#Exercicio 3    
def pictureex3(request):
    t = loader.get_template('livapp/exe3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex3n2(request):
    t = loader.get_template('livapp/exe3n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex3n3(request):
    t = loader.get_template('livapp/exe3n3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex3n4(request):
    t = loader.get_template('livapp/exe3n4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturereforco3(request):
    t = loader.get_template('livapp/reforco3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
       
def picturereforcoex3n2(request):
    t = loader.get_template('livapp/reforcoex3n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedica3(request):
    t = loader.get_template('livapp/dica3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedicaex3n2(request):
    t = loader.get_template('livapp/dicaex3n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    

    
    
#Exercicio 4

def pictureex4(request):
    t = loader.get_template('livapp/exe4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
 
def pictureex4n2(request):
    t = loader.get_template('livapp/exe4n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex4n3(request):
    t = loader.get_template('livapp/exe4n3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex4n4(request):
    t = loader.get_template('livapp/exe4n4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturereforco4(request):
    t = loader.get_template('livapp/reforco4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  

def picturereforcoex4n2(request):
    t = loader.get_template('livapp/reforcoex4n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedica4(request):
    t = loader.get_template('livapp/dica4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturedicaex4n2(request):
    t = loader.get_template('livapp/dicaex4n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
    
    
#Exercicio 5

def pictureex5(request):
    t = loader.get_template('livapp/exe5.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
 
def pictureex5n2(request):
    t = loader.get_template('livapp/exe5n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex5n3(request):
    t = loader.get_template('livapp/exe5n3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex5n4(request):
    t = loader.get_template('livapp/exe5n4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturereforco5(request):
    t = loader.get_template('livapp/reforco5.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  

def picturereforcoex5n2(request):
    t = loader.get_template('livapp/reforcoex5n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedica5(request):
    t = loader.get_template('livapp/dica5.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturedicaex5n2(request):
    t = loader.get_template('livapp/dicaex5n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
    
    
#Exercicio 6

def pictureex6(request):
    t = loader.get_template('livapp/exe6.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
 
def pictureex6n2(request):
    t = loader.get_template('livapp/exe6n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex6n3(request):
    t = loader.get_template('livapp/exe6n3.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def pictureex6n4(request):
    t = loader.get_template('livapp/exe6n4.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturereforco6(request):
    t = loader.get_template('livapp/reforco6.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  

def picturereforcoex6n2(request):
    t = loader.get_template('livapp/reforcoex6n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
def picturedica6(request):
    t = loader.get_template('livapp/dica6.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
def picturedicaex6n2(request):
    t = loader.get_template('livapp/dicaex6n2.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request)) 
    
################################################################################   


#Final

def final(request):
    t = loader.get_template('livapp/final.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))  
    
    
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
        print(request.POST)
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


def post_create_user(request):
    print("AQUI 1")
    if(request.method == 'GET'):

        print("AQUI 2")
     
        print("AQUI 3")
        post_user = request.GET.get('username')
        post_key = request.GET.get('key')
        print(post_user)
        print(post_key)
        print(request)

        new_post = Usuarios( user=post_user, key=post_key)                
        new_post.save()
        retorno = {"status": "ok"}
        print(retorno)
        return JsonResponse(retorno)
   

###########################




###########################
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
    
#def contador(request):  
#    if(request.method == 'GET'):    
#        post_exercicio = request.GET.get('exercicio')
#        post_tempo = request.GET.get('tempo')
#        post_acerto = request.GET.get('acerto')
#        post_erro = request.GET.get('erro')
#        post_tentativa = request.GET.get('tentativa')
#        post_latencia = request.GET.get('latencia')
#        post_coordenadaX = request.GET.get('coordenadaX')
#        post_coordenadaY = request.GET.get('coordenadaY')
#        now = timezone.now()
#        new_post = Contador(exercicio=post_exercicio, tempo=post_tempo, acerto=post_acerto, erro=post_erro, tentativa = post_tentativa, latencia = post_latencia, coordenadaX = post_coordenadaX, coordenadaY = post_coordenadaY, date = now)
#        #new_post = form.save(commit=False)
#        new_post.aluno = request.user                  
#        new_post.save()
#    return redirect('livapp:avatar')
   
   

   
def contador(request):  
    if(request.method == 'GET'):    
        post_exercicio = request.GET.get('exercicio')
        post_tempo = (0 if request.GET.get('tempo') is None else request.GET.get('tempo'))
        post_acerto = request.GET.get('acerto')
        post_erro = request.GET.get('erro')
        post_tentativa = (0 if request.GET.get('tentativa') is None else request.GET.get('tentativa'))
        post_latencia = (0 if request.GET.get('latencia') is None else request.GET.get('latencia'))
        
        
        post_coordenadaX = (0 if request.GET.get('coordenadaX') is None else request.GET.get('coordenadaX'))
        post_coordenadaY = (0 if request.GET.get('coordenadaY') is None else request.GET.get('coordenadaY'))
        post_latencia2 = (0 if request.GET.get('latencia2') is None else request.GET.get('latencia2'))
        post_coordenadaX2 = (0 if request.GET.get('coordenadaX2') is None else request.GET.get('coordenadaX2'))
        post_coordenadaY2 = (0 if request.GET.get('coordenadaY2') is None else request.GET.get('coordenadaY2'))
        post_latencia3 = (0 if request.GET.get('latencia3') is None else request.GET.get('latencia3'))
        post_coordenadaX3 = (0 if request.GET.get('coordenadaX3') is None else request.GET.get('coordenadaX3'))
        post_coordenadaY3 = (0 if request.GET.get('coordenadaY3') is None else request.GET.get('coordenadaY3'))
        post_latencia4 = (0 if request.GET.get('latencia4') is None else request.GET.get('latencia4'))
        post_coordenadaX4 = (0 if request.GET.get('coordenadaX4') is None else request.GET.get('coordenadaX4'))
        post_coordenadaY4 = (0 if request.GET.get('coordenadaY4') is None else request.GET.get('coordenadaY4'))
        now = timezone.now()
        new_post = Contador(exercicio=post_exercicio, tempo=post_tempo, acerto=post_acerto, erro=post_erro, tentativa = post_tentativa, latencia = post_latencia, coordenadaX = post_coordenadaX, coordenadaY = post_coordenadaY, latencia2 = post_latencia2, coordenadaX2 = post_coordenadaX2, coordenadaY2 = post_coordenadaY2, latencia3 = post_latencia3, coordenadaX3 = post_coordenadaX3, coordenadaY3 = post_coordenadaY3, latencia4 = post_latencia4, coordenadaX4 = post_coordenadaX4, coordenadaY4 = post_coordenadaY4, date = now)
        #new_post = form.save(commit=False)
        new_post.aluno = request.user                  
        new_post.save()
    return redirect('livapp:avatar')   
   
   
   
def parametros(request):  
    if(request.method == 'GET'): 
        post_tempoIdeal = request.GET.get('tempoIdeal')
        post_tempoSatisfatorio  = request.GET.get('tempoSatisfatorio')
        post_reforcoForte = request.GET.get('reforcoForte')
        post_reforcoMedio = request.GET.get('reforcoMedio')
        post_reforcoFraco = request.GET.get('reforcoFraco') 
        post_pontuacaoMaxima = request.GET.get('pontuacaoMaxima')
        post_pontuacaoMedia = request.GET.get('pontuacaoMedia')
        post_pontuacaoMinima = request.GET.get('pontuacaoMinima')
        post_pontuacaoFinal = request.GET.get('pontuacaoFinal')
        now = timezone.now()
        new_post = Parametro(tempoIdeal=post_tempoIdeal, tempoSatisfatorio=post_tempoSatisfatorio, reforcoForte=post_reforcoForte, reforcoMedio=post_reforcoMedio, reforcoFraco=post_reforcoFraco, pontuacaoMaxima=post_pontuacaoMaxima, pontuacaoMedia=post_pontuacaoMedia, pontuacaoMinima=post_pontuacaoMinima, pontuacaoFinal=post_pontuacaoFinal, date = now)
        #new_post = form.save(commit=False)
        new_post.aluno = request.user                  
        new_post.save()
    return redirect('livapp:avatar')  
    
    
def getparametro(request):
    retorno = {"tempoIdeal":"5",
               "tempoSatisfatorio":"15",
               "reforcoForte":"1.3",
               "reforcoMedio":"1.2",
               "reforcoFraco":"1.1",
               "pontuacaoMaxima":"10",
               "pontuacaoMedia":"5",
               "pontuacaoMinima":"1",
               "pontuacaoFinal":"115",
            }
    
    
    try:
    
        parametro = Parametro.objects.filter(aluno_id = request.user).order_by('-date').first()
        if parametro:
            print (getattr(parametro,'tempoIdeal'))
            print (getattr(parametro,'tempoSatisfatorio'))
            print (getattr(parametro,'reforcoForte'))
            print (getattr(parametro,'reforcoMedio'))
            print (getattr(parametro,'reforcoFraco'))
            print (getattr(parametro,'pontuacaoMaxima'))
            print (getattr(parametro,'pontuacaoMedia'))
            print (getattr(parametro,'pontuacaoMinima'))
            print (getattr(parametro,'pontuacaoFinal'))
            
            
            retorno = {"tempoIdeal":getattr(parametro,'tempoIdeal'),
                       "tempoSatisfatorio":getattr(parametro,'tempoSatisfatorio'),
                       "reforcoForte":getattr(parametro,'reforcoForte'),
                       "reforcoMedio":getattr(parametro,'reforcoMedio'),
                       "reforcoFraco":getattr(parametro,'reforcoFraco'),
                       "pontuacaoMaxima":getattr(parametro,'pontuacaoMaxima'),
                       "pontuacaoMedia":getattr(parametro,'pontuacaoMedia'),
                       "pontuacaoMinima":getattr(parametro,'pontuacaoMinima'),
                       "pontuacaoFinal":getattr(parametro,'pontuacaoFinal'),
                    }
            
            
            
        
            return JsonResponse(retorno)     
        else:
            return JsonResponse(retorno)
    except:
        return JsonResponse(retorno)

def saveparametro(request):
   if(request.method == 'GET'): 
        post_tempoIdeal = request.GET.get('tempoIdeal')
        post_tempoSatisfatorio  = request.GET.get('tempoSatisfatorio')
        post_reforcoForte = request.GET.get('reforcoForte')
        post_reforcoMedio = request.GET.get('reforcoMedio')
        post_reforcoFraco = request.GET.get('reforcoFraco') 
        post_pontuacaoMaxima = request.GET.get('pontuacaoMaxima')
        post_pontuacaoMedia = request.GET.get('pontuacaoMedia')
        post_pontuacaoMinima = request.GET.get('pontuacaoMinima')
        post_pontuacaoFinal = request.GET.get('pontuacaoFinal')
        now = timezone.now()
        new_post = Parametro(tempoIdeal=post_tempoIdeal, tempoSatisfatorio=post_tempoSatisfatorio, reforcoForte=post_reforcoForte, reforcoMedio=post_reforcoMedio, reforcoFraco=post_reforcoFraco, pontuacaoMaxima=post_pontuacaoMaxima, pontuacaoMedia=post_pontuacaoMedia, pontuacaoMinima=post_pontuacaoMinima, pontuacaoFinal=post_pontuacaoFinal, date = now)
        #new_post = form.save(commit=False)
        new_post.aluno = request.user                  
        new_post.save()
        return  HttpResponse(None)
   
   
   
   
   
   
def latencia(request):  
    if(request.method == 'GET'):    
        post_exercicio = request.GET.get('exercicio')
        post_tentativa = request.GET.get('tentativa')
        post_latencia = request.GET.get('latencia')
        post_coordenadax = request.GET.get('coordenadax')
        post_coordenaday = request.GET.get('coordenaday')
        new_post = Contador(exercicio=post_exercicio, tentativa = post_tentativa, latencia = post_latencia, coordenadax = post_coordenadax, coordenaday = post_coordenaday)
        #new_post = form.save(commit=False)
        new_post.aluno = request.user                  
        new_post.save()
    return redirect('livapp:avatar')  







@login_required
def desempenho_sessao(request):

    pontuacaoSessao = int(getattr(parametro,'pontuacaoSessao'))
    
    form = PostForm()
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            post_pontuacaoSessao = form.cleaned_data['pontuacaoSessao']
            new_post = DesempenhoSessao( pontuacaoSessao='pontuacaoSessao')
            new_post = form.save(commit=False)
            new_post.aluno = request.user                  
            new_post.save()
            retorno = {"status": "ok"}
            print(retorno)
            return JsonResponse(retorno)
            #return redirect('livapp:avatar')
    #elif(request.method == 'GET'):
        #return render(request, 'livapp/avatar.html', {'form': form})















    

