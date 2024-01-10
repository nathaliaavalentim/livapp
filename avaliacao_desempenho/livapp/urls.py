from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static



from .views import *

from . import views

app_name = 'livapp'
urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('<slug:slug>', views.post_detail, name='post_detail'),
    #path('criar/', views.post_create, name='post_create'),
    #path('sobre-nos/', views.about, name='about'),
    #path('contato/', views.contact, name='contact'),
    
    
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('qlearning/', views.qlearning, name='qlearning'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
  
    path('', views.IndexView.as_view(), name='index'),
    

    path('cadastrar_usuario/post_create_user/', views.post_create_user, name='post_create_user'),
    path('avatar/', views.avatar, name='avatar'),
    path('parametro/', views.parametro, name='parametro'),

    
    path('picture/', views.picture, name='picture'),
    
    path('pictureex/', views.pictureex, name='pictureex'),
    path('picturereforco/', views.picturereforco, name='picturereforco'),
    path('picturedica/', views.picturedica, name='picturedica'),
    
    path('pictureex2/', views.pictureex2, name='pictureex2'),
    path('picturereforco2/', views.picturereforco2, name='picturereforco2'),
    path('picturedica2/', views.picturedica2, name='picturedica2'),
    
    path('pictureex3/', views.pictureex3, name='pictureex3'),
    path('picturereforco3/', views.picturereforco3, name='picturereforco3'),
    path('picturedica3/', views.picturedica3, name='picturedica3'),
    
    path('pictureex4/', views.pictureex4, name='pictureex4'),
    path('picturereforco4/', views.picturereforco4, name='picturereforco4'),
    path('picturedica4/', views.picturedica4, name='picturedica4'),
    
    path('pictureex5/', views.pictureex5, name='pictureex5'),
    path('picturereforco5/', views.picturereforco5, name='picturereforco5'),
    path('picturedica5/', views.picturedica5, name='picturedica5'),
    
    path('pictureex6/', views.pictureex6, name='pictureex6'),
    path('picturereforco6/', views.picturereforco6, name='picturereforco6'),
    path('picturedica6/', views.picturedica6, name='picturedica6'),
    
    #Nível 2
    
    path('pictureex1n2/', views.pictureex1n2, name='pictureex1n2'),
    path('picturereforcoex1n2/', views.picturereforcoex1n2, name='picturereforcoex1n2'),
    path('picturedicaex1n2/', views.picturedicaex1n2, name='picturedicaex1n2'),
    
    path('pictureex2n2/', views.pictureex2n2, name='pictureex2n2'),
    path('picturereforcoex2n2/', views.picturereforcoex2n2, name='picturereforcoex2n2'),
    path('picturedicaex2n2/', views.picturedicaex2n2, name='picturedicaex2n2'),
    
    path('pictureex3n2/', views.pictureex3n2, name='pictureex3n2'),
    path('picturereforcoex3n2/', views.picturereforcoex3n2, name='picturereforcoex3n2'),
    path('picturedicaex3n2/', views.picturedicaex3n2, name='picturedicaex3n2'),
    
    path('pictureex4n2/', views.pictureex4n2, name='pictureex4n2'),
    path('picturereforcoex4n2/', views.picturereforcoex4n2, name='picturereforcoex4n2'),
    path('picturedicaex4n2/', views.picturedicaex4n2, name='picturedicaex4n2'),
    
    path('pictureex5n2/', views.pictureex5n2, name='pictureex5n2'),
    path('picturereforcoex5n2/', views.picturereforcoex5n2, name='picturereforcoex5n2'),
    path('picturedicaex5n2/', views.picturedicaex5n2, name='picturedicaex5n2'),
    
    path('pictureex6n2/', views.pictureex6n2, name='pictureex6n2'),
    path('picturereforcoex6n2/', views.picturereforcoex6n2, name='picturereforcoex6n2'),
    path('picturedicaex6n2/', views.picturedicaex6n2, name='picturedicaex6n2'),
    
    #Nível 3
    
    path('pictureex1n3/', views.pictureex1n3, name='pictureex1n3'),    
    path('pictureex2n3/', views.pictureex2n3, name='pictureex2n3'),    
    path('pictureex3n3/', views.pictureex3n3, name='pictureex3n3'),
    path('pictureex4n3/', views.pictureex4n3, name='pictureex4n3'),
    path('pictureex5n3/', views.pictureex5n3, name='pictureex5n3'),
    path('pictureex6n3/', views.pictureex6n3, name='pictureex6n3'),

    #Nível 4
    
    path('pictureex1n4/', views.pictureex1n4, name='pictureex1n4'),    
    path('pictureex2n4/', views.pictureex2n4, name='pictureex2n4'),    
    path('pictureex3n4/', views.pictureex3n4, name='pictureex3n4'),
    path('pictureex4n4/', views.pictureex4n4, name='pictureex4n4'),
    path('pictureex5n4/', views.pictureex5n4, name='pictureex5n4'),
    path('pictureex6n4/', views.pictureex6n4, name='pictureex6n4'),

    


       
   
  ###############################################
    #Homes - Upload
    
    
    path(r'pictureex/upload/', views.upload, name="upload"),
        
    re_path(r'^$', views.homer, name="homer"),
    path(r'picturereforco/upload/', views.upload, name="upload"),
    
    re_path(r'^$', views.homed, name="homed"),
    path(r'picturedica/upload/', views.upload, name="upload"), 
    
    ##############################
    
    #Exercício 1:
    
    re_path(r'^$', views.home, name="home"),
    path(r'pictureex/upload/', views.upload, name="upload"),     
       
    re_path(r'^$', views.home12, name="home12"),
    path(r'pictureex1n2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home13, name="home13"),
    path(r'pictureex1n3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home14, name="home14"),
    path(r'pictureex1n4/upload/', views.upload, name="upload"), 
    
    
    ##############################
    
    #Exercício 2:
    
    re_path(r'^$', views.home21, name="home21"),
    path(r'pictureex2/upload/', views.upload, name="upload"),     
       
    re_path(r'^$', views.home22, name="home22"),
    path(r'pictureex2n2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home23, name="home23"),
    path(r'pictureex2n3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home24, name="home24"),
    path(r'pictureex2n4/upload/', views.upload, name="upload"), 
    
    
    ##############################
    
    #Exercício 3:
    
    re_path(r'^$', views.home31, name="home31"),
    path(r'pictureex3/upload/', views.upload, name="upload"),     
       
    re_path(r'^$', views.home32, name="home32"),
    path(r'pictureex3n2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home33, name="home33"),
    path(r'pictureex3n3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home34, name="home34"),
    path(r'pictureex3n4/upload/', views.upload, name="upload"),     


    ##############################
    
    #Exercício 4:
    
    re_path(r'^$', views.home41, name="home41"),
    path(r'pictureex4/upload/', views.upload, name="upload"),     
       
    re_path(r'^$', views.home42, name="home42"),
    path(r'pictureex4n2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home43, name="home43"),
    path(r'pictureex4n3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home44, name="home44"),
    path(r'pictureex4n4/upload/', views.upload, name="upload"),     


    ##############################
    
    #Exercício 5:
    
    re_path(r'^$', views.home51, name="home51"),
    path(r'pictureex5/upload/', views.upload, name="upload"),     
       
    re_path(r'^$', views.home52, name="home52"),
    path(r'pictureex5n2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home53, name="home53"),
    path(r'pictureex5n3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home54, name="home54"),
    path(r'pictureex5n4/upload/', views.upload, name="upload"),   
    
    
    ##############################
    
    #Exercício 6:
    
    re_path(r'^$', views.home61, name="home61"),
    path(r'pictureex6/upload/', views.upload, name="upload"),     
       
    re_path(r'^$', views.home62, name="home62"),
    path(r'pictureex6n2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home63, name="home63"),
    path(r'pictureex6n3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home64, name="home64"),
    path(r'pictureex6n4/upload/', views.upload, name="upload"),  
    
    
    #Avatar
    re_path(r'^salvaavatar/', views.salvaavatar, name="salvaavatar"),
    path(r'avatar/salvaavatar/', views.salvaavatar, name="salvaavatar"),
    
    re_path(r'^salvaavatarbd/', views.salvaavatarbd, name="salvaavatarbd"),
    path(r'picturereforco3/salvaavatarbd/', views.salvaavatarbd, name="salvaavatarbd"),
    

        

    re_path(r'^recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'picture/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureex/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureexrep1/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureex2/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureexrep2/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureex3/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureexrep3/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    
    path('final/', views.final, name='final'),
    
    
    
    #Modelo
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #Contador
    re_path(r'^contador/', views.contador, name="contador"),
    path(r'pictureex/contador/', views.contador, name="contador"),
    path(r'pictureex2/contador/', views.contador, name="contador"),
    path(r'pictureex3/contador/', views.contador, name="contador"),
    path(r'pictureex4/contador/', views.contador, name="contador"),
    path(r'pictureex5/contador/', views.contador, name="contador"),
    path(r'pictureex6/contador/', views.contador, name="contador"),
    path(r'pictureex1n2/contador/', views.contador, name="contador"),
    path(r'pictureex2n2/contador/', views.contador, name="contador"),
    path(r'pictureex3n2/contador/', views.contador, name="contador"),
    path(r'pictureex4n2/contador/', views.contador, name="contador"),
    path(r'pictureex5n2/contador/', views.contador, name="contador"),
    path(r'pictureex6n2/contador/', views.contador, name="contador"),
    path(r'pictureex1n3/contador/', views.contador, name="contador"),
    path(r'pictureex2n3/contador/', views.contador, name="contador"),
    path(r'pictureex3n3/contador/', views.contador, name="contador"),
    path(r'pictureex4n3/contador/', views.contador, name="contador"),
    path(r'pictureex5n3/contador/', views.contador, name="contador"),
    path(r'pictureex6n3/contador/', views.contador, name="contador"),
    path(r'pictureex1n4/contador/', views.contador, name="contador"),
    path(r'pictureex2n4/contador/', views.contador, name="contador"),
    path(r'pictureex3n4/contador/', views.contador, name="contador"),
    path(r'pictureex4n4/contador/', views.contador, name="contador"),
    path(r'pictureex5n4/contador/', views.contador, name="contador"),
    path(r'pictureex6n4/contador/', views.contador, name="contador"),
    
    
    #qlearning
    re_path(r'^qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex4/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex5/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex6/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex1n2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex2n2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex3n2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex4n2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex5n2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex6n2/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex1n3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex2n3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex3n3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex4n3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex5n3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex6n3/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex1n4/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex2n4/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex3n4/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex4n4/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex5n4/qlearning/', views.qlearning, name="qlearning"),
    path(r'pictureex6n4/qlearning/', views.qlearning, name="qlearning"),

    
    #Latencia
    re_path(r'^latencia/', views.latencia, name="latencia"),
    path(r'pictureex2/latencia/', views.latencia, name="latencia"),
    
    re_path(r'^getparametro/', views.getparametro, name="getparametro"),
    path(r'parametro/getparametro/', views.getparametro, name="getparametro"),
    
    re_path(r'^saveparametro/', views.saveparametro, name="saveparametro"),
    path(r'parametro/saveparametro/', views.saveparametro, name="saveparametro"),
    
    


]




